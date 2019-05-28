#coding=utf-8
import time
import json
import random
import base64
import requests
import urllib
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
def autoSelect():
    #根据浏览器类型选择方法   火狐：Firefox    Chrome：Chrome   ie：IE
    #后面的是你的浏览器对应根目录
    driver = webdriver.Firefox(executable_path= r"C:\Program Files\Mozilla Firefox\geckodriver.exe")
    #将问卷星网站放在下面
    driver.get('https://www.wjx.cn/jq/40371185.aspx')
 
    time.sleep(1)
 
    #单选题
    xpath1 = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[1]/div[2]/ul/li[%s]/a' % str(random.randint(1,4))
    answer_1 = driver.find_elements_by_xpath(xpath1)[0]
    answer_1.click()
    time.sleep(1)
 
    xpath2 = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/ul/li[%s]/a' % str(random.randint(1,4))
    answer_2 = driver.find_elements_by_xpath(xpath2)[0]
    answer_2.click()
    time.sleep(1)
 
    
    #提交
    submit=driver.find_element_by_xpath('//*[@id="submit_table"]')
    submit.click()
    #submit = driver.find_element_by_xpath('//*[@id="submit_button"]')
    #submit.click()
    #因为反爬虫机制，不可以直接点按钮，要点table对象
 
    time.sleep(2)
    driver.quit()

 
 
if __name__ == '__main__':
    #循环4次（不要一次太多，不然会有反爬虫机制（验证码））
    for index in range(1,11):
        autoSelect()