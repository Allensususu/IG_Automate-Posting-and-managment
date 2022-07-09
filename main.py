from ctypes.wintypes import WORD
from email import message
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
import otherfunction 
import login_ig
import get_contact
from webdriver_manager.chrome import ChromeDriverManager
import post
import xlrd
import shutil
import os
import follow

_worksheet = (xlrd.open_workbook("account.xls", formatting_info=True))
worksheet = _worksheet.sheet_by_name('account')
worksheet_col = 1 #account , password , ig_name , real_name , stat(pass) , post , follower
worksheet_row = 1 

img= ''
post_word = ''
tag= ''
other_account=[]

hash_tag = []

url = 'https://www.instagram.com/'  



if __name__ == '__main__' :
    for i in range (worksheet.nrows)::
        account  = worksheet.cell(i+1 , 0).value
        password = worksheet.cell(i+1, 1).value
        account_name = worksheet.cell(i+1 , 2).value
        post_ = worksheet.cell(i+1 , 6).value
        follower = worksheet.cell(i+1 , 7).value
        following = worksheet.cell(i+1 , 8).value
        if worksheet.cell(i+1, 5).value == "":
            continue
        print(account)
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(url)

        ######function 
        otherfunction.read_cookie(browser,account)
        login_ig.login(account,password,browser)
        otherfunction.get_follower_post(browser,account_name,i)
        #follow.auto_follow(other_account , browser, post_)
        #get_contact.get_pic(account_name ,browser); break
        otherfunction.save_cookie(browser,account)
        post.post(browser,account)
        browser.close


