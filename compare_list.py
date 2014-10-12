# -*- coding: utf-8 -*-
import random
import string
import PyPDF2
import subprocess
#import urllib2
#import urllib
#from selenium import webdriver
#import request

def compare_list(list1, list2):
    #lst = list(list2)
    for y in list1:
        print y
    print ""
    print ""
    newl = []
    for z in list2:
        newl.append(''.join(z))#convert tuple to string
    print newl
        
    status = 0
    newlist = []
    for x in list1:
        if x not in newl:
            status = 1
            newlist.append(x)

    if status == 0:
        return "ok, username in UI & database matches"
    else:
        return "fail UI doesn't contain next user name(s) %s" %str(newlist)

def check_username(list1, a):
    newl = []
    li = []
    status = 0
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for z in list1:
        newl.append(''.join(z))#convert tuple to string
    for item in list1:
        if a in newl:
            status = 1
        else:
            return a
    if status == 1:
        N=8
        #print ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))
        return ''.join(random.choice(chars) for _ in range(N))
        '''#ascii alphabet of all alphanumerals
        r = (range(48, 58) + range(65, 91) + range(97, 123))
        random.shuffle(r)
        return reduce(lambda i, s: i + chr(s), r[:random.randint(0, len(r))], "")'''
        '''
        for k in range(1, 8):
            li.append(random.choice(chars))
            li = "".join(li)
        print li'''

def slice_string(list1, user):
    l = []
    for c in list1:
        s = c.rsplit('_', 1)
        #print s
        x = s[1].rsplit('.pdf', 1)
        #print x #x[0] contains username
        l.append(x[0])
    #print l

    str_begin = "TCS_0319KESKIMAAOSK_"
    str_end = ".pdf"
    str_full = ""
    for y in l:
        #print y
        if y == user:
            str_full = "%s%s%s" %(str_begin,y,str_end)
            return y
            #return ''.join([str_begin, y, str_end])
            #return str_full
            #return str("TCS_0319KESKIMAAOSK_"+y+".pdf".encode('latin1'))
    print ''.join([str_begin, y, str_end])

def getPDFContent(path):
    #print "input path %s" %path
    path.encode("ascii", "ignore")
    #pt = path.encode('utf-8').strip()
    #print "pt value %s"%pt
    content = ""
    num_pages = 1
    p = file(path, "rb")
    pdf = PyPDF2.PdfFileReader(p)
    for i in range(0, num_pages):
        content += pdf.getPage(i).extractText() + "\n\r"
        #print content
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content

def Remove_Whitespace(instring):
    return str(instring.replace(" ", ""))

def find_string(a,b):#a = basic string, b = find what
    if a.find(b) != -1:
        return b

def find_string_list(alist,user):
    dlist = alist.split("Username:")
    #print "d value is %s"%dlist
    plist = alist.split("Fixed")    
    nlist = []
    f = 1
    for z in plist:
        nlist.append(z)
        #print f
        f = f + 1
        #print "Z val %s "%z

    print nlist[0]
    #user="aas"
    if nlist[0].find(user) != -1:
        return "ok"
    else:
        return "fail"

def execute_batch():
    filepath="C:\\Robot_Repo\\trunk\\robot-tcs\\tcs-mgmt\\tcsmgmt.bat"
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print p.returncode # is 0 if success
'''
def read_pdf():
    #fp.set_preference("browser.download.dir",getcwd())
    #fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")

    #browser = webdriver.Firefox(firefox_profile=fp)
    req = urllib2.Request('tcs-mgmt/adduser.html')
    #browser = webdriver.Firefox() # Get local session of firefox
    #browser.get("tcs-mgmt/adduser.html") # Load page
    #response = urllib2.urlopen(req)
    #pdffile = urllib2.urlopen("https://t1-dmz-tcsmgmt-1/tcs-mgmt/adduser.html")
    #data = pdffile.read()
    #with open('file.data', 'wb') as file:
    #    file.write(req.content)
    print "file contains %s " %req
    #output = open('test.pdf','wb')
    #output.write(pdffile.read())
    #output.close()
    return "ok"
           



d = read_pdf()
print d
'''

execute_batch()
#path = "C:\\Robot_Repo\\trunk\\robot-tcs\\tcs-mgmt\\NewUserPdf\\TCS_0319KESKIMAAOSK_timotestaaja.pdf"
#c = getPDFContent(path)
#print c
#dlist = c.split("Username:")
#print "d value is %s"%dlist
#plist = c.split("Fixed")
#print "p value is %s"%plist
#s = "0319 KESKIMAA OSKKauppakätu 2440101 Jyväskylä Name: aaasUsername: aasFixed password: xidT5fvtE-mail: as@ss.fiMobile phone number: 01 9C4D41FF26 27252A4702 5E9D1D5027 BB97FC7F03 562CE71A28 0025C53D04 C9F8CFE529 AA1CA83205 511B2F1830 3254BAFC06 8BCBCC9E31 4295987507 3CDF56FB32 1DFE797B08 4D865E3133 6CCED3C109 FD4E8D8034 D08DB8EC10 194886B835 F08F1DE711 BD36D64236 DEEB36C812 8CD7118737 DBC0E24E13 8898A14E38 436E1B4A14 28DDFB2239 74C144B915 F97252DD40 44340EDC16 A79E2F8841 3A2C0AD517 6FE3356E42 57D62D9418 AF1B0A2843 6FA9B6B019 2CB8DB2144 E875441A20 E45C695B45 378042C621 B3D738C846 90D7BAA622 AB3DE64947 AD58A8FD23 C57827E148 6DBF757324 3537919549 F3DB1E0125 8D55A71E50 86ACFF19"
#f = "aas"
#g = find_string_list(s,f)
#print g
#s = Remove_Whitespace("TCS_0319KESKIMAAOSK_ aas.pdf")
#print s
#lis = ['TCS_0319KESKIMAAOSK_1timotestaaja.pdf', 'TCS_0319KESKIMAAOSK_aas.pdf', 'TCS_0319KESKIMAAOSK_afasfas.pdf']
#a = slice_string(lis, "aas")
#print a
#a1 = ['timotestaaja']
#a2 = ['timotestaaja']

#a1 = ['04885721','aas','afasfas','asdas','cheek','dasfasfasfd','ddsfasdgfasdfasd','fasafasasf','gdfsdffs','gdsgsgs','gsdsgsds','henrih','jargo','robot','theena','timotestaaja']
#a2 = ['henrih','cheek','theena','robot','jargo','afasfas','04885721','aas','ddsfasdgfasdfasd','fasafasasf','gdsgsgs','asdas','dasfasfasfd','gdfsdffs','gsdsgsds','timotestaaja']

#c = compare_list(a1, a2)
#print c


#a1 = ['timotestaaja','cat','dog']
#a = 'cat'
#v = check_username(a1, a)
#print v
