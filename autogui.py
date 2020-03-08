import pyautogui as pag
import time

# pag.screenshot("youtube.png",region=(67, 112, 120, 40))
i = pag.locateCenterOnScreen("youtube.png")
print(i)
pag.click(i)

#77 201