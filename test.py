#coding=utf-8
import time
import random
from selenium import webdriver

def rand_pick(seq , probabilities):
    '''随机数
            指定随机序列和概率，选取序列中的对象
           
        Args：
            seq：指定的序列，必须为可迭代对象
            probabilities：序列中对应索引下元素的概率
    '''
    assert len(seq)==len(probabilities) and abs((sum(probabilities)-1))<1e-3
    x = random.uniform(0 ,1)
    cumprob = 0.0
    for item , item_pro in zip(seq , probabilities):
        cumprob += item_pro
        if x < cumprob:
            break
    return item


def ratio(driver,xpath,placeholder='placeholder',choice_number=4,distribution=None,sleep_time=0.8):
    """单选题
            定义单选题的随机回答


        Args：
            driver：驱动
            xpath：抓取到的html对象（选项）
            placeholder：占位符，用于标记选项的位置
            choice_number：选项数
            distribution：选项概率分布，默认平均分布
            sleep_time：答题后等待时间
    """
    assert xpath.count(placeholder)==1,'mismatched placeholder!!!'
    if distribution is None : distribution=[1/choice_number]*choice_number
    random_option=rand_pick(list(range(1,choice_number+1)),distribution)
    xpath=xpath.replace(placeholder,str(random_option))
    answer=driver.find_elements_by_xpath(xpath)[0]
    answer.click()
    time.sleep(sleep_time)

def double(driver,xpath,placeholder='placeholder',choice_number=4,distribution=None,sleep_time=0.8):
    """双选题
            定义双选题的随机回答


        Args：
            driver：驱动
            xpath：抓取到的html对象（选项）
            placeholder：占位符，用于标记选项的位置
            choice_number：选项数
            distribution：选项概率分布，默认平均分布
            sleep_time：答题后等待时间
    """
    assert choice_number>=2
    assert xpath.count(placeholder)==1,'mismatched placeholder!!!'
    if distribution is None : distribution=[1/choice_number]*choice_number
    random_option=rand_pick(list(range(1,choice_number+1)),distribution)
    random_option_2=rand_pick(list(range(1,choice_number+1)),distribution)
    while random_option_2==random_option:
        random_option_2=rand_pick(list(range(choice_number)),distribution)
    xpath1=xpath.replace(placeholder,str(random_option))
    xpath2=xpath.replace(placeholder,str(random_option_2))
    answer=driver.find_elements_by_xpath(xpath1)[0]
    answer.click()
    answer=driver.find_elements_by_xpath(xpath2)[0]
    answer.click()
    time.sleep(sleep_time)

def checkbox(driver,xpath,placeholder='placeholder',choice_number=4,threshold=None,sleep_time=0.8):
    """多选题
            定义多选题的随机回答


        Args：
            driver：驱动
            xpath：抓取到的html对象（选项）
            placeholder：占位符，用于标记选项的位置
            choice_number：选项数
            threshold：阈值（若随机数大过该值，则点击该选项，越大则该选项越难被选中）默认为0.5
            sleep_time：答题后等待时间
    """
    assert xpath.count(placeholder)==1,'mismatched placeholder!!!'
    if threshold is None : threshold=[0.5]*choice_number
    random_option=random.randint(1,choice_number)
    xpath_1 = xpath.replace(placeholder,str(random_option))
    answer = driver.find_elements_by_xpath(xpath_1)[0]
    answer.click()
    time.sleep(sleep_time)
    for i in range(choice_number):
        xpath_1=xpath.replace(placeholder,str(i+1))
        answer = driver.find_elements_by_xpath(xpath_1)[0]
        if random.random()>threshold[i] and (i+1) != random_option:
            answer.click()
            time.sleep(sleep_time)

def textaera(driver,xpath,keys="hahaha~",sleep_time=0.8):
    """文本题
            自定义回答的文本框


        Args：
            driver：驱动
            xpath：抓取到的html对象（选项）
            keys：填充的文本
            sleep_time：答题后等待时间
    """
    answer = driver.find_elements_by_xpath(xpath)[0]
    answer.send_keys(keys)
    time.sleep(sleep_time)



def autoSelect():
    #根据浏览器类型选择方法   火狐：Firefox    Chrome：Chrome   ie：IE
    #后面的是你的浏览器对应根目录
    driver = webdriver.Firefox(executable_path= r"C:\Program Files\Mozilla Firefox\geckodriver.exe")

    #将问卷星网站放在下面
    driver.get('https://www.wjx.cn/jq/40371185.aspx')
 
    #单选题
    xpath1 = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[1]/div[2]/ul/li[placeholder]/a'
    ratio(driver,xpath1)

    #多选题
    xpath2 = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/ul/li[placeholder]/a'
    checkbox(driver,xpath2)

    #文本框
    xpath3='//*[@id="q3"]'
    textaera(driver,xpath3)
    
    #提交
    submit=driver.find_element_by_xpath('//*[@id="submit_table"]')
    submit.click()
    #submit = driver.find_element_by_xpath('//*[@id="submit_button"]')
    #submit.click()
    #因为反爬虫机制，不可以直接点按钮，要点table对象
 
    time.sleep(1)
    driver.quit()

 
if __name__ == '__main__':
    #循环10次（不要一次太多，不然会有反爬虫机制（验证码））
    for index in range(1,11):
        autoSelect()

