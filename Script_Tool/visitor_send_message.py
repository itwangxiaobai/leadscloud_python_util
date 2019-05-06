# -*- coding: utf-8 -*-
# @Time: 2019/5/6 9:39
# @Author : Yang DaWei
# @Project : LeadsCloud
# @FileName: visitor_send_message.py
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')
for i in range(1000):
    # chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    string = "automation program sends message number " + str(1+i) + " " + "at " + current_time
    try:
        chrome_driver.get("http://www.yialife.co.za/contact.html")
        chrome_driver.implicitly_wait(30)
        chrome_driver.find_element_by_xpath("//*[@id='messageText']").send_keys(string)
        time.sleep(3)
        chrome_driver.find_element_by_xpath("//*[@id='sendBtn']").click()
        time.sleep(3)
        print(string)
        chrome_driver.delete_all_cookies()
        chrome_driver.quit()
    except NoSuchElementException as e:
        print("fail to send number" + string)
        raise e








