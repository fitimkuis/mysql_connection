# -*- coding: utf8 -*-
import pyPdf  
def getPDFContent(path):
    content = ""
    num_pages = 1
    p = file(path, "rb")
    pdf = pyPdf.PdfFileReader(p)
    for i in range(0, num_pages):
        content += pdf.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content

def create_profile(self):
    from selenium import webdriver
    fp =webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir",'C:\\Users\\Timo\\Desktop\\url')
    #fp.set_preference("browser.helperApps.neverAsk.saveToDisk",'application/pdf')
    fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain, application/pdf, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    fp.set_preference("browser.helperApps.alwaysAsk.force", False);
    fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
    fp.set_preference("pdfjs.disabled", True) 
    fp.update_preferences()
    return fp.path


f= open('test.txt','w')
pdfl = getPDFContent("test.pdf").encode("ascii", "ignore")
f.write(pdfl)
print "Done..."
f.close()
