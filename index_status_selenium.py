
#coding: utf-8

import re
import unittest
import time
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

class DaIndexing(object):
    driver = webdriver.Firefox(executable_path=r'C:\Users\fred\Documents\webdrivers\geckodriver.exe')
    S = "*************************************************************************************"

    def SetUp(self):
        driver = self.driver
        S = self.S
        driver.maximize_window()
        location2 = "http://inbtlwl17:12048/da/component/main?__dmfClientId=1552312588487&__dmfTzoff=240"
        try:
            driver.get(location2)
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "component/main?")) )
            time.sleep(30)
        except UnexpectedAlertPresentException:
            print "XSS - WAITING FOR THE SERVER CREDENTIALS *********"
            print("**********************************************")
            time.sleep(30)
        print("DaIndexing SetUp()")

    def LoGin(self):
        driver = self.driver
        S = self.S
        Lusername = r"C:\Python27\da-testing-login-python\official-selenium-login\bdgcqauser.txt"
       with open(Lusername, 'r') as psfile:
            Loginuser =  [ base64.b64decode(line) for line in psfile]
        driver.find_element_by_id("LoginUsername").send_keys(Loginuser)
        time.sleep(5)

       
        print("Getting encrypted passord **************************************************")
        Lpass = r"C:\Python27\da-testing-login-python\official-selenium-login\bdgcpss.txt"
        with open(Lpass, 'r') as psfile:
            password = [ base64.b64decode(line) for line in psfile]
        print("Using encrypted passord **************************************************")
        driver.find_element_by_id("LoginPassword").send_keys(password)
        time.sleep(5)
        print("Validating Login in button and sending that info ")
        time.sleep(4)
        Xpath = "/html/body/form/div/div[3]/div/div[2]/button"
        Button = driver.find_element_by_xpath(Xpath).click()
        print("Login  Succcessful")
        print("DaIndexing LoGin()")
        time.sleep(30)

    def DefaultFrame(self):
        driver = self.driver
        S = self.S
        print("Switching to  default content ")
        driver.switch_to.default_content()
        print("DaIndexing DefaultFrame()")
        print(S)

    def locatingIndexFrame(self):
        driver = self.driver
        S = self.S
        Mainv = driver.find_element_by_id("MainEx_view_0")
        if Mainv:
            driver.switch_to.frame(Mainv)
            time.sleep(4)
            print("Switched to  to MainEx_view Successfully")
            print("**********************************")       
            print("Switching to  Classic_toolbar_0 Frame")
            print(S)
            print("Switching to  Classic_browser_0 Frame")
            Browser = driver.find_element_by_id("Classic_browser_0")
            if Browser:
                driver.switch_to.frame(Browser)
                time.sleep(4)
                print("Switched to  to Classic_browser Successfully")
                print("************************ **********")     
            print("Finding BrowserTree_0 Tree")
            print("**********************************")
            Tree = driver.find_element_by_id('BrowserTree_0')
            if Tree:
                print(Tree.text)
            print("Finding Indexing Management")
            print("**********************************")
            IndexMngmnt = driver.find_element_by_link_text("Indexing Management")
            if IndexMngmnt:
                print(IndexMngmnt.tag_name)
                print(IndexMngmnt.is_enabled)
                print(IndexMngmnt.is_selected)
                Click = IndexMngmnt.click()
                time.sleep(4)
                print("Switched to  to Classic_browser Successfully")
                print("************************ **********")
                print("DaIndexing locatingIndexFrame()")
                time.sleep(30)
               
    def locatingIndexAgentServersFrame(self):
        driver = self.driver
        S = self.S
        print("Handling Indexing Agent and Servers status section ")
        print(S) 
        print("Switching to the default frame ")
        driver.switch_to.default_content()
        print(S)
        time.sleep(2)
        print("Handling MainView  Frame ")
        print(S)
        mainV = driver.find_element_by_id("MainEx_view_0")
        driver.switch_to.frame(mainV)
        time.sleep(2)
        print(S)

        print("Handling Classic_workarea Frame")
        #driver.find_element_by_id("Classic_workarea_0")
        Workarea = driver.find_element_by_id("Classic_workarea_0")
        driver.switch_to.frame(Workarea)
        time.sleep(2)
        print(S)

        print("Handling Content Froms")
        driver.find_element_by_id("Form_content_0")
        Formcount = driver.find_element_by_id("Form_content_0")
        driver.switch_to.frame(Formcount)
        print(S)
        print("All frames processed Successfully")
        print(S)
        print("Checking index process Status")
        print(S)

        IndagntServer = driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[4]/td[2]/a")
        if IndagntServer:
            print(S)
            print(IndagntServer.is_enabled)
            print(IndagntServer.is_selected)
            Click = IndagntServer.click()
            print(S)
            print("Successfully Openned index Status Window")
            print(S)
            print("DaIndexing locatingIndexAgentServersFrame ()")

        time.sleep(2)


    def openIndexStatus(self):
        driver = self.driver
        S = self.S
        print("Displaying Server Index status")
        try:
            Class = driver.find_element_by_id("IndexAgentServerList_0")
            if Class:
                Table = driver.find_element_by_tag_name("table")
                if Table:
                    Trs = driver.find_element_by_tag_name("tr")
                    if Trs:
                        print(S)
                        print("On the right Frame")
                        Indexstatus = driver.find_element_by_xpath("/html/body/form/div/div[4]/table/tbody/tr[3]/td[8]")
                        time.sleep(2)
                        Index_Status = Indexstatus.text
                        print("System Index status is: {}".format(Index_Status))
                        print(S)

        except NoSuchElementException as err:
            print("Sorry Unable to locate Test elements Specified!!: Test Failed:: {}::".format(err))
            print(S)
            print("Saving screen shot for index status")
            driver.save_screenshot("indexstatus.png")
            print(S)
            print("THE END")
            time.sleep(20)


    def altered(self):
        driver = self.driver
        S = self.S
        print("Parent explicited()")
        driver.quit()


if __name__ == "__main__":
    da = DaIndexing()
    da.SetUp()
    da.LoGin()
    da.DefaultFrame()
    da.locatingIndexFrame()
    da.locatingIndexAgentServersFrame()
    da.openIndexStatus()
    da.altered()
	
