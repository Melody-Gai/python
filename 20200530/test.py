from selenium import webdriver
import time
from selenium.webdriver.common.key import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os


import os
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("乃万")
driver.find_element_by_id("su").click()
driver.maximize_window()
time.sleep(8)