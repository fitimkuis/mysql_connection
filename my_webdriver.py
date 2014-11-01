from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


class my_webdriver(object):

    def __init__(self):
        pass

    def vaadin(self):
        driver = webdriver.Firefox()
        driver.get("http://demo.vaadin.com/dashboard/")
        driver.implicitly_wait(2) # seconds

        o = my_webdriver()
        yes = o.find_element(driver,"gwt-uid-4")
        print yes
            
        elem = driver.find_element_by_id("gwt-uid-4")
        elem.send_keys("timo")
        elem = driver.find_element_by_id("gwt-uid-6")
        elem.send_keys("timo")
        driver.find_element_by_xpath(".//*[@id='ROOT-2521314']/div/div[2]/div/div/div/div[3]/div/div[5]/div").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath(".//*[@id='ROOT-2521314']/div/div[2]/div/div[1]/div/div/div[4]/div[2]/span/span[2]").click()
        driver.implicitly_wait(1)
        driver.find_element_by_css_selector(".v-button.v-widget.clearbutton.v-button-clearbutton").click()

        driver.implicitly_wait(1)
        driver.find_element_by_css_selector(".v-filterselect-button").click()
  
        driver.find_element_by_xpath("//div[@id='VAADIN_COMBOBOX_OPTIONLIST']/div/div[2]/table/tbody/tr[6]/td/span").click()

        

        driver.find_element_by_xpath(".//*[@id='ROOT-2521314']/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[3]/div/div[1]/div/div[2]").click()


        
    def find_element(self,driver,by_id):
        e = driver.find_element_by_id(by_id)
        if (e.get_attribute("disabled")=='true'):
            return False
        return e
    
    def my_driver(self):
        driver = webdriver.Firefox()
        driver.get("http://adactin.com/HotelApp/")
        
        assert "AdactIn.com - Hotel Reservation System" in driver.title
        elem = driver.find_element_by_xpath(".//*[@id='username']")
        elem.send_keys("fitimkuis")
        #elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath(".//*[@id='password']")
        elem.send_keys("ModeeMi16")
        driver.find_element_by_xpath(".//*[@id='login']").click()
        #driver.find_element_by_xpath(".//*[@id='location']")
        select = Select(driver.find_element_by_id("location"))
        select.select_by_visible_text("Sydney")

        select = Select(driver.find_element_by_id("hotels"))
        select.select_by_visible_text("Hotel Creek")

        select = Select(driver.find_element_by_id("room_type"))
        select.select_by_visible_text("Standard")

        select = Select(driver.find_element_by_id("room_nos"))
        select.select_by_visible_text("1 - One")

        elem = driver.find_element_by_name("datepick_out")
        elem.send_keys("19/10/2014")

        elem = driver.find_element_by_name("datepick_in")
        elem.send_keys("20/10/2014")

        select = Select(driver.find_element_by_id("adult_room"))
        select.select_by_visible_text("1 - One")

        select = Select(driver.find_element_by_id("child_room"))
        select.select_by_visible_text("1 - One")

        driver.find_element_by_xpath(".//*[@id='Submit']").click()

        driver.find_element_by_id("radiobutton_0").click()

        driver.find_element_by_xpath(".//*[@id='continue']").click()

        elem = driver.find_element_by_xpath(".//*[@id='first_name']")
        elem.send_keys("Mat")
        elem = driver.find_element_by_xpath(".//*[@id='last_name']")
        elem.send_keys("Nickersson")

        elem = driver.find_element_by_xpath(".//*[@id='address']")
        elem.send_keys("Home")

        elem = driver.find_element_by_xpath(".//*[@id='cc_num']")
        elem.send_keys("1234567890123456")

        select = Select(driver.find_element_by_xpath(".//*[@id='cc_type']"))
        select.select_by_visible_text("American Express")
        
        select = Select(driver.find_element_by_xpath(".//*[@id='cc_exp_month']"))
        select.select_by_visible_text("January")

        select = Select(driver.find_element_by_xpath(".//*[@id='cc_exp_year']"))
        select.select_by_visible_text("2014")

        elem = driver.find_element_by_xpath(".//*[@id='cc_cvv']")
        elem.send_keys("123")

        driver.find_element_by_xpath(".//*[@id='book_now']").click()

        driver.find_element_by_id("logout").click()
        #driver.find_element_by_xpath(".//*[@id='my_itinerary']").click()
        
                
        #elem.send_keys(Keys.RETURN)
        #driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[2]").click
        assert "No results found." not in driver.page_source
        #driver.close()
        return driver.title
        
OBJECT = my_webdriver()    
'''   
    String baseUrl = "http://newtours.demoaut.com";
    String expectedTitle = "Welcome: Mercury Tours";
    String actualTitle = "";

    // launch Firefox and direct it to the Base URL
    driver.get(baseUrl);

    // get the actual value of the title
    actualTitle = driver.getTitle();

    /*
     * compare the actual title of the page witht the expected one and print
     * the result as "Passed" or "Failed"
     */
    if (actualTitle.contentEquals(expectedTitle)){
        System.out.println("Test Passed!");
    } else {
        System.out.println("Test Failed");
    }

    //close Firefox
    driver.close();

    // exit the program explicitly
    System.exit(0);
'''
