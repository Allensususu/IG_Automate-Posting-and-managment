from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
import otherfunction
from ctypes.wintypes import WORD
from email import message
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def auto_follow(meme_account,browser , post): 
    if int(float(post)) > 30 :
        x = random.randint(0,len(meme_account)-1)
        browser.get("https://www.instagram.com/" + str(meme_account[x]) )
        #//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span')))
        follow_click = browser.find_elements_by_class_name('g47SY ')[1]
        follow_click.click()
        time.sleep(5)
        follow_button = browser.find_elements_by_class_name('sqdOP.L3NKy.y3zKF     ') 
        
        temp = 0
        y = random.randint(20,30)
        while len(follow_button) < y :
            modal = browser.find_element_by_class_name('isgrP')   
            #modal = browser.find_element_by_xpath('/html/body/div[6]/div/div/div')    
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)      
            follow_button = browser.find_elements_by_class_name('sqdOP.L3NKy.y3zKF     ') 
            
            if temp == len(follow_button):
                continue
            temp = len(follow_button)
            

        for i in range(len(follow_button)):
            time.sleep(random.randint(3,8))
            follow_button[i].click()
        
        time.sleep(10)

def no_follow(account_name,browser):
    pass
    