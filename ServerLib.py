""" Robot library for testing E-Commerce Server API

* Keywords for sending and verifying Server API HTTP commands
* Requires m2crypto (Python interface to OpenSSL library)

"""

import os, sys
import locale
import urllib, urllib2, urlparse
import binascii, re
from M2Crypto import RSA
import hashlib

class ServerLib:
    """ Robot keywords """

    def __init__(self):
        self.__parameters = {}
        self.__expected = {}
        self.__response = {}
        self.__savedInvalidValues = []
        self.__server = None

    def setUrl(self, url):
        #print "debug url "+str(url)
        self.__server = ServerInterface(url)
        print "debug server interface "+str(self.__server)

    def add_parameter(self, key, value):
        """ Add parameter, which will be sent with Send Message keyword """
        self.__parameters[key] = str(value)

    def send_message(self, signatureType='1', customSignature=None):
        """ Send message containing parameters given with Add Parameter Keyword """
        self.__response = {}
        print "server" +str(self.__server)
        print "debug" +str(self.__parameters)
        recv = self.__server.sendAndReceive(self.__parameters,
                                    signatureType, customSignature)
        
        print "Received:", recv

        if len(recv) <= 1:
            print "Nothing received?"
        else:
            self.__saveResponse(recv)

        print ""
        self.__parameters = {}

    def add_expected(self, key, value):
        """ Add expected parameter value, this is checked with Verify Response.
            If value is '*', any value is accepted """
        self.__expected[key] = str(value)

    def verify_response(self, flags=None):
        """ Verify that expected parameters were received. 
            If 'exactMatch' is given as parameter, number of received key/value 
            pairs must be same as given with Add Expected keyword """

        if len(self.__response) == 0:
           raise TestFailed("No reply from server") 

        if flags == "exactMatch":
            if len(self.__response) != len(self.__expected):
                print "FAIL. Got %d keys, expected %d"%(len(self.__response), 
                                                    len(self.__expected))
                for k in self.__expected:
                    if not (k in self.__response):
                        print "Key in expected but not in response:", k

                for k in self.__response:
                    if not (k in self.__expected):
                        print "Key in response but not in expected:", k

                raise TestFailed("Number of keys is different than expected.")
            else:
                print "Correct number of keys found"

        """ Verify keys and values """
        for k, v in self.__expected.iteritems():
            # keys belonging to a group (<N>) are handled later
            if re.findall(r"[\S\s]*-<N[\d]+>$", k):
                continue

            print "Verifying that %s=%s is found"%(k, v)
            if k in self.__response:
                if v == '*':
                    print "PASS"
                elif self.__response[k] == v:
                    print "PASS"
                else:
                    print "FAIL"
                    raise TestFailed("Incorrect value for %s: %s, should be %s"%(k, 
                                                self.__response[k], v))
            else:
                print "FAIL"
                raise TestFailed("Key not found: %s"%(k))

        """ Verify groups of <N> keys, there can be multiple in random (?) order """
        # find groups of expected keys ending with <N?> from test case
        expKeyGroups = [[] for k in range(0,100)]
        for k in self.__expected.keys():
            match = re.match(r"[\S\s]*-<N(\d+)>$", k)
            if match:
                expKeyGroups[int(match.group(1))].append(k)

        expKeyGroups = [g for g in expKeyGroups if g != []]
        #print "Expected key Groups:", expKeyGroups

        # find groups of keys ending with <N> from response
        keyGroups = [[] for k in range(0,100)]
        for k in self.__response.keys():
            match = re.match(r"[\S\s]*-(\d+)$", k)
            if match:
                keyGroups[int(match.group(1))].append(k)

        keyGroups = [g for g in keyGroups if g != []]
        #print "Key Groups:", keyGroups

        # check that any of the groups match expected groups
        for expGroup in expKeyGroups:
            # check there is matching group with some value of <N>
            print "Matching parameter group:"
            for e in expGroup:
                print "%s=%s"%(e, self.__expected[e])
            
            groupFound = False

            for keyGroup in keyGroups:
                # match values for each expected key
                # find out index
                groupIndex = re.match(r"[\S\s]*-([\d]+)$", keyGroup[0]).group(1)
                found = False
                for expKey in expGroup:
                    # remove <N>
                    expKeyBeginning = re.match(r"([\S\s]+)<N([\d]+)>$", expKey).group(1)
                    keyInGroup = expKeyBeginning + groupIndex
                    if not keyInGroup in keyGroup:
                        found = False
                        break # expected key not found

                    if (self.__expected[expKey] != '*') and \
                        (not self.__response[keyInGroup] == self.__expected[expKey]):
                        found = False
                        break # values do not match

                    found = True
                if found:
                    groupFound = True
                    print "Found match:"
                    for k in keyGroup:
                        print "%s=%s"%(k, self.__response[k])
            
            print ""
            if not groupFound:
                raise TestFailed("Did not find matching group of response parameters")
        
        self.__expected = {}

    def verify_no_response(self):
        """ Verify that there was no response from server """
        if len(self.__response) == 0:
            print "No response from server as expected. PASS"
        else:
            print "Response should not have been received from server. FAIL"
            raise TestFailed("Response was received.")

    def verify_not_found(self, key):
        """ Verify that the given key is not found in response
            (but a response is expected). """

        if len(self.__response) == 0:
            print "No response from server. FAIL"
            raise TestFailed("No response from server.")
        else:
            if key in self.__response:
                print "Key %s shouldn't be found. FAIL"%(key)
                raise TestFailed("Key shouldn't be found: %s"%(key))
        
        print "Key %s not found. PASS"%(key)

    def test_missing_fields(self):
        """ Send several messages where one of the parameters is missing.
            There should be no response from server. """
        for k, v in self.__parameters.iteritems():
            # remove one field
            params = self.__parameters.copy()
            del params[k]
            print "Sending without field %s=%s"%(k,v)
            recv = self.__server.sendAndReceive(params)
            if len(recv) <= 1:
                print "No response to invalid message. PASS.\n"
            else:
                print "Received response for invalid message:", recv
                print "FAIL"
                raise TestFailed("Received response for invalid message")

        print "All PASSED."
   
    def save_invalid_value(self, key, value, expected="NoReply"):
        """ Save invalid value to be tested later in loop """
        self.__savedInvalidValues.append((key, value, expected))
        
    def count_saved_invalid_values(self):
        return len(self.__savedInvalidValues)
    
    def test_saved_invalid_value(self):
        """ Test first saved invalid value which was saved earlier """
        if len(self.__savedInvalidValues) == 0:
            raise SystemError("No saved invalid values")
        key, value, expected = self.__savedInvalidValues.pop(0)
        self.test_invalid_value(key, value, expected)
        
        self.__parameters = {}
        self.__expected = {}

    def test_invalid_value(self, key, value, expected="NoReply"):
        """ Send message with invalid value in given field"""
        params = self.__parameters.copy()
        params[key] = value
        print "========================================================"
        print "Sending %s=%s, expecting %s"%(key, value, expected)
        recv = self.__server.sendAndReceive(params)

        if len(recv) <= 1:
            if expected == "NoReply":
                print "No reply as expected - PASS.\n"
            else:
                raise TestFailed("No reply, expected '%s' - FAIL.\n" % (expected))
        else:
            print "Received response:", recv
            self.__saveResponse(recv)
            print ""
            error = None

            if expected == "PASS" and not ("s-f-1-30_error-message" in self.__response):
                print "No errors as excepted - PASS.\n"
                return
                #raise TestFailed("Expected no reply - FAIL.\n")

            if expected == "NoReply":
                raise TestFailed("Expected no reply - FAIL.\n")
            
            if expected == "NoError":
                print "Expected valid reply - PASS.\n"
                return

            if "s-f-1-30_error-message" in self.__response:
                error = self.__response["s-f-1-30_error-message"]
            
                if expected == error:
                    print "Received error message '%s' as expected - PASS\n" % (error)
                else:
                    raise TestFailed("Received error message '%s', expected '%s' - FAIL\n" % (error, expected))
            else:
                raise TestFailed("No error message, expected '%s' - FAIL\n" % (expected))
        
    def test_invalid_values(self, value):
        """ Send several messages where one of parameters has invalid value."""
        for k, v in self.__parameters.iteritems():
            self.test_invalid_value(k, value)

        print "All tested. Check admin web log for exception alerts!"

    def query_response_value(self, key):
        """ Get value for the given key """
        return self.__response[key]

    def __saveResponse(self, recv):
        # decode from application/x-www-form-urlencoded
        self.__response = {}
        
        for pair in urlparse.parse_qsl(recv):
            if pair[0] in self.__response:
                raise TestFailed("Received several fields with key %s"%(pair[0]))

            self.__response[pair[0]] = pair[1]

        print ""
        print "Response from server:"
        for k, v in self.__response.iteritems():
            print "%s=%s"%(k, v)

        # check signature of response

        # "openssl dgst -sha1 -verify ../resources/server_publickey.pem 
        #    -signature signature.txt message.txt"

        sortedKeys = sorted(self.__response.keys())
        sortedTuples = [(key, self.__response[key]) for key in sortedKeys]

        msg = ""
        for key in sortedKeys:
            # ; in value must be replaced with ;;
            if not 'signature' in key:
                msg += "%s=%s;"%(key, self.__response[key].replace(';',';;'))
        
        if 's-t-256-256_signature-one' in self.__response:
            signatureBytes = binascii.a2b_hex(self.__response['s-t-256-256_signature-one'])
            
            keyPath = os.path.join(os.path.dirname(__file__), 'server_publickey.pem')
            pkey = RSA.load_pub_key(keyPath)
            
            result = None
            try:
                result = pkey.verify(hashlib.sha1(msg.encode('utf-8')).digest(), 
                                            signatureBytes, algo='sha1')
            except Exception as e:
                raise TestFailed("Response sha1 validation failed: " + str(e))

            if not result:
                raise TestFailed("Response sha1 validation failed.")

        if 's-t-256-256_signature-two' in self.__response:
            signatureBytes = binascii.a2b_hex(self.__response['s-t-256-256_signature-two'])
            
            keyPath = os.path.join(os.path.dirname(__file__), 'server_publickey.pem')
            pkey = RSA.load_pub_key(keyPath)

            result = None
            try:
                result = pkey.verify(hashlib.sha512(msg.encode('utf-8')).digest(), 
                                            signatureBytes, algo='sha512')
            except Exception as e:
                raise TestFailed("Response sha512 validation failed: " + str(e))

            if not result:
                raise TestFailed("Response sha512 validation failed.")

    def encrypt_card_details(self, pan, expiry):
        """ Encrypt data for field s-f-256-512_encrypted-card-details """ 
        keyPath = os.path.join(os.path.dirname(__file__), 'server_publickey.pem')
        pkey = RSA.load_pub_key(keyPath)

        data = pan + "=" + expiry
        encrypted = pkey.public_encrypt(data.encode('utf-8'), RSA.pkcs1_padding)
        encryptedHex = binascii.b2a_hex(encrypted).upper()

        print "Card details encrypted:", data

        return encryptedHex
 
class ServerInterface:
    """ Low level sending and receiving functionality """

    def __init__(self, url):
        self.url = url
       
    def sendAndReceive(self, parameters, signatureType='1', customSignature=None):
        """ Send and receive.
            parameters: dict of keys and values,
            signatureType: '1', '2', 'both', 'none',
            customSignature: can be given for testing wrong signature """

        sortedKeys = sorted(parameters.keys())
        sortedTuples = [(key, parameters[key]) for key in sortedKeys]

        msg = ""
        for key in sortedKeys:
            # ; in value must be replaced with ;;
            msg += "%s=%s;"%(key, parameters[key].replace(';',';;'))

        # Add signatures
        if signatureType != 'none':
            
            keyPath = os.path.join(os.path.dirname(__file__), 'privatekey.pem')
            pkey = RSA.load_key(keyPath)

            # create signature 1
            if signatureType == '1' or signatureType == 'both':
                try:
                    signatureBytes1 = pkey.sign(hashlib.sha1(msg.encode('utf-8')).digest(),
                                                        algo='sha1')
                except Exception as error:
                    print "Creating signature 1 failed."
                    raise error
                signature1 = binascii.b2a_hex(signatureBytes1).upper()

                if customSignature:
                    signature1 = customSignature
                sortedTuples.append(("s-t-256-256_signature-one", signature1))

            # create signature 2 
            if signatureType == '2' or signatureType == 'both':
                try:
                    signatureBytes2 = pkey.sign(hashlib.sha512(msg.encode('utf-8')).digest(), 
                                                    algo='sha512')
                except Exception as error:
                    print "Creating signature 2 failed:", error
                    raise error
                signature2 = binascii.b2a_hex(signatureBytes2).upper()

                if customSignature:
                    signature2 = customSignature
                sortedTuples.append(("s-t-256-256_signature-two", signature2))
 
        # print logging
        print "Sending:"
        for pair in sortedTuples:
            print "%s=%s"%(pair[0], pair[1])
        
        print ""

        # encode data first as utf-8, because urlencode won't accept non-ascii
        strTuples = []
        try:
            for pair in sortedTuples:
                strTuples.append((pair[0].encode('utf-8'), 
                                    pair[1].encode('utf-8')))
        except Exception as error:
            print "UTF-8 encoding failed for", pair
            raise

        # encode content as application/x-www-form-urlencoded
        try:
            data = urllib.urlencode(strTuples)
        except Exception as error:
            print "application/x-www-form-urlencoded encoding of message failed"
            raise error

        # HTTP sending
        print "Sending data:", data
        req = urllib2.Request(self.url, data)
        u = urllib2.urlopen(req, timeout=90)
        resp = u.read()
        u.close()

        return resp

class TestFailed(Exception):
    pass

