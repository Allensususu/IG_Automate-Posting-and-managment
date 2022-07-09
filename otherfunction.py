import requests
import os 
import pickle
from selenium import webdriver 
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as Soup
import os
import random, string
import requests
import json
import xlwt
from xlutils.copy import copy
import xlrd


def download_img(pic,name):
    os.makedirs('./unclassify/',exist_ok=True)
    url=pic
    r=requests.get(url)
    with open('./unclassify/' +name+ '.jpg','wb') as f:
        f.write(r.content)
        

def save_cookie(browser,account):
    cookies = browser.get_cookies()
    with open("./cookies/"+ account +".json", 'w') as f:
        f.write(json.dumps(cookies))


def read_cookie(browser,account):
    try :
        with open("./cookies/"+ account +".json", 'r', encoding='utf-8') as f:
            cookie_list = json.loads(f.read())
        for cookie in cookie_list:
            browser.add_cookie(cookie)
        browser.refresh() 

    except FileNotFoundError :
        with open("./cookies/"+ account +".json", 'w', encoding='utf-8') as f:
            f.write ("")

def return_post_contact(browser):
    try:
        post_contact = browser.find_element_by_css_selector('._7UhW9.xLCgt.MMzan.KV-D4.se6yk.T0kll').text
        post_contact = post_contact.partition('\n')[0]
        return post_contact
    except:
        pass

def get_follower_post(browser,account_name,i ):
    worksheet = (xlrd.open_workbook("account.xls", formatting_info=True))
    new_worksheet = copy(worksheet)
    _worksheet = new_worksheet.get_sheet(0)
    
    try:
        
        browser.get("https://www.instagram.com/" + account_name)
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'g47SY ')))
        post = browser.find_elements_by_class_name('g47SY ')[0].text
        follower = browser.find_elements_by_class_name('g47SY ')[1].text
        following = browser.find_elements_by_class_name('g47SY ')[2].text
        #follwer =  browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span').text
        #post = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/div/span').text
        _worksheet.write (i+1 , 6 , post)
        _worksheet.write (i+1 , 7 , follower)
        _worksheet.write (i+1 , 8 , following)
        new_worksheet.save('account.xls')
    except Exception as e:
        print(e)
        print("----------------")


