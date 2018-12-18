#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

path = "C:\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")



#"https://accounts.google.com/signin/chrome/sync/identifier?ssp=1&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifDesktopChromeSync"

#element = driver.find_element_by_class("website-title")
element_id = driver.find_element_by_name("username") 


element_pw = driver.find_element_by_name("password")
element_id.send_keys("")
element_pw.send_keys("")
element_pw.submit()
                  


#driver.close()
#html = requests.get("chrome://history/")
#print html.text

#if __name__=="__main__":
    
