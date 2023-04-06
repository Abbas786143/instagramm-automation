from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import string
import pyautogui
import urllib.request
from selenium.webdriver.chrome.options import Options
from PIL import Image
from pathlib import Path
urllist=[]
import os
import csv
import pyautogui

with open('description.csv', 'r') as f:
  data1 = csv.reader(f)
  data = list(data1)
dir_path = "E:/new projects of python/tasks/Insta Auto Upload/data"
# list to store files
res = []
i=0
videoname=[]
i=0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

import pandas as pd
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=../googleProfile")
chrome_options.add_argument("--remote-debugging-port=9222")

browser = uc.Chrome(use_subprocess=True,options=chrome_options)
for name in res:
    browser.get("https://www.instagram.com/")
    create=browser.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div/div[1]/div')
    create.click()
    time.sleep(5)
    
    upload=browser.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input')
    upload.send_keys(dir_path+"/"+name)
    time.sleep(5)
    create1=browser.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
    create1.click()
    time.sleep(5)
    create2=browser.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
    create2.click()
    time.sleep(5)
    des=browser.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/p')
    des.send_keys(data[i])
    time.sleep(5)
    create3=browser.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
    create3.click()
    time.sleep(5)
    i=i+1
    
