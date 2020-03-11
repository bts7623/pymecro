import pyautogui as pag
import time

# 해당 URL 새탭으로 열기
def open_new_tab(URL):
    pag.hotkey("ctrl","t") # 새 탭 생성
    time.sleep(1)
    pag.typewrite(URL)
    pag.typewrite(["enter"])

# 해당 이미지 더블 클릭
def dclick_on_image(img):
    p = pag.locateCenterOnScreen(img)
    pag.doubleClick(p)

# 해당 이미지 클릭
def click_on_image(img):
    p = pag.locateCenterOnScreen(img)
    pag.Click(p)

# 어디서 어디까지 드래그 앤 드롭
def drag_and_drop(fromX,fromY,toX,toY):
    pag.moveTo(fromX, fromY)
    pag.dragTo(x=toX, y=toY, duration=2)