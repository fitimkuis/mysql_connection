
# modules we're using (you'll need to download lxml)
import lxml.html, urllib2, urlparse, os
import urllib
import requests
import wget  #pip install wget

class pdf():

    def download_os(self):
        # if you comment out this line, it will download to the directory from which you run the script.
        os.chdir('C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\testdir')
        url = 'http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf'
        print urllib.urlretrieve(url)
    
    def download(self,url):
        #print url
        file_url = url
        #file_url = 'http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf'
        file_name = wget.download(file_url)
        if len(file_name) != 0:
            return file_name
        else:
            return "download fail"

    
    def getpdf(self,burl):
        # the url of the page you want to scrape
        base_url = burl
        #base_url = 'http://www.novapdf.com/kb/pdf-example-files-created-with-novapdf-138.html'
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
            d.download(x)
            return x
            #print node.attrib['href']
        #data = urllib2("http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf")
        #urllib.url_retrive("http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf","c://home")
        #print data
        #,"C:\\Users\\Timo\\Desktop\\url"

    def create_profile(self,dirpath):
        print "Debug saving path "+dirpath
        from selenium import webdriver
        fp =webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir",dirpath)
        #fp.set_preference("browser.download.dir",'C:\\Users\\Timo\\Desktop\\url')
        #fp.set_preference("browser.helperApps.neverAsk.saveToDisk",'application/pdf')
        fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain, application/pdf, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        fp.set_preference("browser.helperApps.alwaysAsk.force", False);
        fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
        fp.set_preference("pdfjs.disabled", True) 
        fp.update_preferences()
        return fp.path

ob = pdf()
ob.download_os()

#y = ob.getpdf('http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf')
#print "#########################################################"
#print "fetched val is %s "%y

'''    
response = urllib2.urlopen('http://www.novapdf.com/uploads/novapdf_en/media_items/pdf-example-encryption.original.pdf')
html = response.read()
print html
print "##################################################################"
print html[20:50]'''
