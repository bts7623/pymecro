from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome() #크롬 드라이버 사용하겠다.
URL = "https://www.naver.com" #URL 저장
driver.get(URL) #해당 URL을 연다. (크롬으로)
driver.maximize_window() #해당 웹페이지 최대화
action = ActionChains(driver) #제어할 준비

driver.find_element_by_css_selector('.lg_local_btn').click()