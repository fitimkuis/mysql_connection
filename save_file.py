import os
from selenium import webdriver
import time

#url = "http://file-sample.com/xlsx/"
url = "http://www.novapdf.com/kb/pdf-example-files-created-with-novapdf-138.html"

# configuring profile
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', 'C:\\Users\\Timo\\Desktop\\url')
#fp.set_preference("browser.helperApps.neverAsk.saveToDisk",'application/pdf')
fp.set_preference("browser.helperApps.alwaysAsk.force", False);
fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
fp.set_preference("pdfjs.disabled", True) 
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain, application/pdf, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# open the web page and download the file
driver = webdriver.Firefox(firefox_profile=fp)
#driver.maximize_window()
driver.get(url)
#driver.find_element_by_xpath('//div[@class="post-entry"]//a').click()
driver.find_element_by_xpath(".//*[@id='a-slot-content-117-blog-body-1']/ul/li[1]/a").click()
#driver.find_element_by_xpath('.//*[@id=a-slot-content-117-blog-body-1]/ul/li[1]/a').click()
#.//*[@id='a-slot-content-117-blog-body-1']/ul/li[1]/a
time.sleep(3)
driver.close()
