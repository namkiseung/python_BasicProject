#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

path = "C:\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://192.168.177.132:1111/login")



#"https://accounts.google.com/signin/chrome/sync/identifier?ssp=1&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifDesktopChromeSync"

#element = driver.find_element_by_class("website-title")
element_id = driver.find_element_by_name("user_id")
element_id.clear()
element_id.send_keys("i2sec")

element_pw = driver.find_element_by_name("user_pw")
element_pw.clear()
element_pw.send_keys("0000")
element_pw.submit()
                  


#driver.close()
#html = requests.get("chrome://history/")
#print html.text

#if __name__=="__main__":
    
