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

def login(account,password,browser):
    if (EC.presence_of_element_located((By.NAME, 'username'))):
        try:
            url = 'https://www.instagram.com/'  
            browser.get(url) 
            WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))
            username_input = browser.find_elements_by_name('username')[0]
            password_input = browser.find_elements_by_name('password')[0]
            print("inputing username and password...")
            username_input.send_keys(account)
            password_input.send_keys(password)
            #登入
            WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
            '//*[@id="loginForm"]/div/div[3]/button/div')))
            login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
            login_click.click()
            time.sleep(3)
            #稍後再說
            #WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
            #store_click = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]
            #store_click.click()
            time.sleep(10)
        except Exception as e:
            pass