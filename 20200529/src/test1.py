from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("乃万")
driver.find_element_by_id("su").submit()
time.sleep(6)
driver.find_element_by_link_text("乃万_百度百科").click()
time.sleep(5)
driver.quit()