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
import otherfunction
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
import random
from webdriver_manager.chrome import ChromeDriverManager


txt_files= []
img_files= []

def post (browser,account):
    hash_tag = ["]
    account_name = "apple________"
    def get_img():
        if img_files == []:
            print("--------------------")
            for file in os.listdir("img/"):
                if file.endswith(".jpg"):
                    img_files.append(file)
                    

        x = random.randint(0,len(img_files)-1)

        return(img_files[x])

    ###打開圖片確認無重複，且不存在檢查檔案自動新建
    if not(os.path.isfile("./cookies/" + account  +'.txt')):
        with open( "./cookies/" + account  +'.txt', 'w') as f:
            f.write("")
    img_file = get_img()
    check = 0
    with open( "./cookies/" + account  +'.txt', 'r') as f:
        while (check != 0 ):
            img_file = get_img()
            if img_file not in f:
                check = 1

        
    with open("img/" + img_file[0:10] + '.txt', 'r',encoding="utf-8") as f:
            fread = f.read()
            message = fread + "\n" 

    avoid_the_same = []
    x = random.randint(10,25)
    tag  = ""
    j=0
    while j < x :
        num = random.randint(0,len(hash_tag)-1)
        if num not in avoid_the_same:
            avoid_the_same.append(num)
            j = j+1
            tag = tag +" " + hash_tag[num]

    print(message)
    print(tag)

    JS_ADD_TEXT_TO_INPUT = """
    var elm = arguments[0], txt = arguments[1];
    elm.value += txt;
    elm.dispatchEvent(new Event('change'));
    """

        

    ########################### Test use

    #url = 'https://www.instagram.com/'  
    #browser = webdriver.Chrome(ChromeDriverManager().install())
    #browser.get(url)
    #otherfunction.read_cookie(browser,account)

    ##########################



    JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"

    def drop_files(element, files, offsetX=0, offsetY=0):
        browser = element.parent
        isLocal = not browser._is_remote or '127.0.0.1' in browser.command_executor._url
        paths = []
        
        # ensure files are present, and upload to the remote server if session is remote
        for file in (files if isinstance(files, list) else [files]) :
            if not os.path.isfile(file) :
                raise FileNotFoundError(file)
            paths.append(file if isLocal else element._upload(file))
        
        value = '\n'.join(paths)
        elm_input = browser.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
        elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

    WebElement.drop_files = drop_files

    #進入主畫面
    browser.get("https://www.instagram.com/" + account_name)
    #點擊上傳按鈕
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="QBdPU "]/*[name()="svg"][@aria-label="新貼文"]')))
    new_post_button = browser.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="新貼文"]')
    new_post_button.click()
    time.sleep(2)
    dropzone = browser.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div")
    # 選擇一個圖片、影片
    dropzone.drop_files(os.path.dirname(os.path.realpath(__file__)) +"/img/" + img_file)
    time.sleep(2)
    # 縮放 (這邊選擇原始比例)
    browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]/div").click()
    # 下一步
    try:
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()
    except:
        pass
    # 內文

    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea").click()
    post = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
    #browser.execute_script(JS_ADD_TEXT_TO_INPUT, post, message)
    #post.send_keys("")
    try:
        post.send_keys(message)
    except:
        try:
            post.send_keys(message[0:-2])
            post.send_keys("\n")
        except :
            print("不支援表情符號")
            raise 

    post.send_keys(tag)
    time.sleep(4)
    browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'img[alt=動畫勾號][class=s4Iyt]')))

    with open( "./cookies/" + account  +'.txt', 'a+') as f:
        f.write(img_file[0:10] + '\n')