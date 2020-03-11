import pyautogui as pag
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

'''
    기본 Setting
    python 설치
    pip install pyautogui
    pip install opencv-python
    pip install selenium
    chromedriver.exe 다운
'''

#JENIFFER SET
driver = webdriver.Chrome() #크롬 드라이버 사용하겠다.
driver.implicitly_wait(3) # 웹 자원 로드 대기
URL = "http://210.107.249.6:7900" #URL 저장
driver.get(URL) #해당 URL을 연다. (크롬으로)
driver.maximize_window() #해당 웹페이지 최대화
action = ActionChains(driver) #제어할 준비

#JENIFFER LOGIN
driver.find_element_by_name("id").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_css_selector(".btn.focus.btn-login").click()
time.sleep(2)
driver.find_element_by_css_selector(".icon-analysis").click()
time.sleep(1)
driver.find_element_by_css_selector(".icon-statistics").click()
pag.hotkey("ctrl","t") # 새 탭 생성
time.sleep(1)
pag.typewrite(URL)
pag.typewrite(["enter"])


#XTRACTOR SET
driver2 = webdriver.Chrome() #크롬 드라이버 사용하겠다.
driver2.implicitly_wait(3) # 웹 자원 로드 대기
URL = "http://210.107.252.165:9090/MCS" #URL 저장
driver2.get(URL) #해당 URL을 연다. (크롬으로)
driver2.maximize_window() #해당 웹페이지 최대화
action = ActionChains(driver2) #제어할 준비

#XTRACTOR LOGIN
driver2.find_element_by_id("userId").send_keys("admin")
driver2.find_element_by_id("password").send_keys("nw1944")
driver2.find_element_by_css_selector(".loginLBtn").click()
time.sleep(2)
p = pag.locateCenterOnScreen("img/xtractor.png")
print(p)
pag.doubleClick(p)
pag.moveRel(None, 23)
time.sleep(1)
pag.click()
pag.hotkey("ctrl","t") # 새 탭 생성
time.sleep(1)
pag.typewrite(URL)
pag.typewrite(["enter"])
time.sleep(3)

#Drag And Drop
pag.moveTo(121, 17)
pag.dragTo(x=-1818, y=18, duration=2)
pag.moveTo(121, 17)
pag.dragTo(x=-1818, y=18, duration=2)
pag.moveTo(121, 17)
pag.dragTo(x=-1818, y=18, duration=2)

'''
Xtractor http://210.107.252.165:9090/MCS admin nw1944
ZENIUS http://172.16.1.37 zenius zenius12345
JENNIFER http://210.107.249.6:7900 admin admin
'''
