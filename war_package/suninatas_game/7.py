#-*- coding:utf-8 -*-
from selenium import webdriver
#import urllib2
import urllib, requests

if __name__=="__main__":
    __id=input("id :")
    __pw="zzzzzzzz"#input("pw :")
    path = "C:\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("http://suninatas.com/main/main.asp")
    driver.find_element_by_css_selector('#login > form > p > input.tb').send_keys(__id)
    driver.find_element_by_css_selector('#login > form > p > input.tb_pw').send_keys(__pw)
    driver.find_element_by_css_selector('#login > form > p > input.btnLogin.gray').click()

    
    alert = driver.switch_to_alert()
    alert.dismiss()
    driver.get("http://suninatas.com/challenge/challenge.asp")
    driver.find_element_by_css_selector('#tabs-1 > table > tbody > tr:nth-child(3) > td:nth-child(2) > button').click()
    driver.find_element_by_css_selector('body > form:nth-child(2) > div:nth-child(74) > input[type="submit"]').click()
    alert.dismiss()

    #driver.quit()
    '''
http://selenium-python.readthedocs.io/navigating.html?highlight=alert
https://cjh5414.github.io/python-selenium-alert/
http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.alert

'''
