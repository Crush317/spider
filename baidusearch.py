from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
browser=Chrome()
browser.get("https://www.baidu.com")
time.sleep(1)
browser.maximize_window()
time.sleep(2)
link=browser.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(browser).move_to_element(link).perform()
browser.find_element_by_link_text('搜索设置').click()
time.sleep(3)
browser.find_element_by_id('nr_3').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()
time.sleep(2)
browser.switch_to_alert().accept()
time.sleep(1)
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').submit()
time.sleep(2)
js="var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(3)
js="var q=document.documentElement.scrollTop=0"
browser.execute_script(js)
time.sleep(3)
browser.close()


