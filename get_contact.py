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


def get_pic(get_pic_account,browser):
    with open('get_stat.txt', 'r') as f:
        fread = f.read()
    with open("get_stat.txt", 'a+') as f:
        post_url = []
        media_url = []
        img_video_name = ""
        count = 0 # 目前獲得圖片連結數
        repeat_post = 0
        for acc in get_pic_account:
            try:
                url = 'https://www.instagram.com/'  +  acc
                browser.get(url)
                time.sleep(2)
                n_scroll = (int(browser.find_elements_by_class_name('g47SY ')[0].text)/6)+3

                for i in range(int(n_scroll)):
                    scroll = 'window.scrollTo(0, document.body.scrollHeight);'
                    browser.execute_script(scroll)
                    html = browser.page_source
                    soup = Soup(html, 'lxml')
                    # 尋找所有的貼文連結
                    for elem in soup.select('article div div div div a'):
                            # 如果新獲得的貼文連結不在列表裡，則加入
                        if elem['href'] in fread:
                            break
                        if elem['href'] not in post_url:
                            post_url.append(elem['href'])
                            f.write(elem['href'] + '\n')
                    time.sleep(2)
            except:
                continue
    f.close

    for media in post_url:
        browser.get('https://www.instagram.com/' + media)
        soup = Soup(browser.page_source,"lxml")
        time.sleep(2)
        try:
            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'ltEKP')))
        except:
            browser.refresh()
            time.sleep(2)
        
        button = None
        if (soup.find(class_="Ckrof") != None):
            button = 1
        while(button != None): # 如果下一頁按鈕存在
            soup = Soup(browser.page_source,"lxml")
            time.sleep(1)
            # 取得網頁元素框架
            img_frame = soup.find_all(class_="Ckrof")
            vid_frame = soup.find_all(class_="_5wCQW")
            # 找圖片連結
            for i in img_frame:
                try:
                    new_img = i.img.get('src')
                    if (new_img != None) & (new_img not in media_url):
                        media_url.append(new_img)
                        count += 1
                        img_video_name = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
                        #otherfunction.download_img( new_img, img_video_name)
                except:
                    pass
            # 找影片連結
            for j in vid_frame:
                try:
                    new_vid = j.video.get("src")
                    if (new_vid != None) & (new_vid not in media_url):
                        media_url.append(new_vid)
                        count += 1
                except:
                    pass
            # 尋找下一頁按紐
            try:
                WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, '_6CZji')))
                button = browser.find_elements_by_class_name('_6CZji')[0]
                button.click()
            except:
                button = None

        else: # 如果有沒有下一頁(單張圖片或影片)
            # 取得網頁元素框架
            soup = Soup(browser.page_source,"lxml")
            img_frame = soup.find(class_="KL4Bh")
            vid_frame = soup.find(class_="_5wCQW")
            # 取得圖片連結並下載
            try:
                new_img = img_frame.img.get('src')
                if (new_img != None):
                    media_url.append(new_img)
                    count += 1
                    img_video_name = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
                    otherfunction.download_img( new_img, img_video_name)
                    
            except:
                pass
            # 取得影片連結
            try:
                new_vid = vid_frame.video.get('src')
                if (new_vid != None):
                    media_url.append(new_vid)
                    count += 1
            except:
                pass

        post_contact = otherfunction.return_post_contact(browser)
        with open("unclassify/" + img_video_name +  ".txt", 'w+', encoding='UTF-8') as s:
             s.write(str(post_contact))

    print("總共取得 " + str(len(post_url)) + " 篇貼文連結")
    print("總共取得: " + str(count) + " 張圖片")

