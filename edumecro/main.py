import pag
import time
import drive_chrome

'''
    기본 Setting
    python 설치
    pip install pyautogui
    pip install opencv-python
    pip install selenium
    chromedriver.exe 다운
'''

#JENIFFER SET
jen = drive_chrome.GetDrive() #크롬 드라이버 사용하겠다.
jend = jen.driver
jend.implicitly_wait(3) # 웹 자원 로드 대기
URL = "http://210.107.249.6:7900" #URL 저장
jend.get(URL) #해당 URL을 연다. (크롬으로)
jend.maximize_window() #해당 웹페이지 최대화

#JENIFFER LOGIN
jen.find_element_by_name("id").send_keys("admin")
jen.find_element_by_name("password").send_keys("admin")
jen.find_element_by_css_selector(".btn.focus.btn-login").click()
time.sleep(2)
jen.find_element_by_css_selector(".icon-analysis").click()
time.sleep(1)
jen.find_element_by_css_selector(".icon-statistics").click()

pag.open_new_tab(URL)


#XTRACTOR SET
xtrc = drive_chrome.GetDrive() #크롬 드라이버 사용하겠다.
xtrcd = xtrc.driver
xtrcd.implicitly_wait(3) # 웹 자원 로드 대기
URL = "http://210.107.252.165:9090/MCS" #URL 저장
xtrcd.get(URL) #해당 URL을 연다. (크롬으로)
xtrcd.maximize_window() #해당 웹페이지 최대화

#XTRACTOR LOGIN
xtrc.find_element_by_id("userId").send_keys("admin")
xtrc.find_element_by_id("password").send_keys("nw1944")
xtrc.find_element_by_css_selector(".loginLBtn").click()

time.sleep(2)
pag.dclick_on_image("img/xtractor.png")
pag.pag.moveRel(None, 23)
time.sleep(1)
pag.pag.click()
pag.open_new_tab(URL)
time.sleep(3)

#Drag And Drop
pag.drag_and_drop(2669, 212, 482, 15)
pag.drag_and_drop(2669, 212, 482, 15)
pag.drag_and_drop(2669, 212, 482, 15)
pag.drag_and_drop(2669, 212, 482, 15)

'''
Xtractor http://210.107.252.165:9090/MCS admin nw1944
ZENIUS http://172.16.1.37 zenius zenius12345
JENNIFER http://210.107.249.6:7900 admin admin
'''
