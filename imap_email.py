# -*- coding: utf-8 -*-

import imaplib
import re

def ret_address():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('fitesterpoint@gmail.com', '%%Qwerty123')
    mail.list()
    # Out: list of "folders"
    mail.select("inbox") # connect to inbox.

    result, data = mail.search(None, "ALL")
     
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1] # get the latest
    #print latest_email_id
     
    result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
     
    raw_email = data[0][1] # here's the body, which is raw text of the whole email
    # including headers and alternate payloads
    #print raw_email

    m = re.findall ('https(.*?)code', raw_email, re.DOTALL)
    #print m[0]
    address = 'https'+m[0]+'code'
    address = address.replace(" ", "")
    address = address.replace("3D", "")
    equal = len(re.findall("=", address))
    saddress = address.split('=')
    caddress = saddress[0]+'='+saddress[1]+""+saddress[2]+'='+saddress[3]
    #print "count of %d "%equal
    #print caddress
    return caddress

#a = ret_address()
#print "######################################"
#print a
#https://t1-dmz-peosweb-1/peos-payment-web/paymentLink?l-f-1-20_link=6074011648&s-f-1-36_mc=line-test-merchant-agreement-code
#match = re.search('https://t1-dmz-peosweb-1/peos-payment-web/paymentLink?', raw_email)
#if match:
#    print match.group()

#print re.search('https', raw_email)
#match = re.search('([\w.-]+)@([\w.-]+)', str)

#print re.group()

#result, data = mail.uid('fetch',latest_email_id , '(X-GM-THRID X-GM-MSGID)')
#re.search('X-GM-THRID (?P<https>\d+) X-GM-MSGID (?P<https>\d+)', data[0]).groupdict()
# this becomes an organizational lifesaver once you have many results returned.
