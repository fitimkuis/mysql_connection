
# modules we're using (you'll need to download lxml)
import lxml.html, urllib2, urlparse
import urllib
import requests
import wget  #pip install wget


class pdf():
    
    def download(self,url):
        print url
        file_url = url
        #file_url = 'http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf'
        file_name = wget.download(file_url)
        if len(file_name) != 0:
            return file_name
        else:
            return "download fail"

    
    def getpdf(self):
        # the url of the page you want to scrape
        base_url = 'http://www.novapdf.com/kb/pdf-example-files-created-with-novapdf-138.html'
        # fetch the page
        res = urllib2.urlopen(base_url)
        # parse the response into an xml tree
        tree = lxml.html.fromstring(res.read())
        # construct a namespace dictionary to pass to the xpath() call
        # this lets us use regular expressions in the xpath
        ns = {'re': 'http://exslt.org/regular-expressions'}
        # iterate over all <a> tags whose href ends in ".pdf" (case-insensitive)
        for node in tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns):
            # print the href, joining it to the base_url
            #print urlparse.urljoin(base_url, node.attrib['href'])
            x = urlparse.urljoin(base_url, node.attrib['href'])
            #print "x val is %s "%x
            d = pdf()
            d.download_pdf(x)
            return x
            #print node.attrib['href']
        #data = urllib2("http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf")
        #urllib.url_retrive("http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf","c://home")
        #print data
        #,"C:\\Users\\Timo\\Desktop\\url"

ob = pdf()
#y = ob.getpdf()
#print "#########################################################"
#print "fetched val is %s "%y

'''    
response = urllib2.urlopen('http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf')
html = response.read()
print html
print "##################################################################"
print html[20:50]'''
