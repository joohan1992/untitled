import pyautogui
import time

# 현재 화면의 크기 반환
width, height = pyautogui.size()
print(width, height)

# 현재 마우스 포인터의 위치 반환
x, y = pyautogui.position()
print(x, y)

time.sleep(2)
pyautogui.keyDown('alt')
time.sleep(0.5)
pyautogui.keyDown('tab')
time.sleep(0.5)
pyautogui.keyUp('tab')
time.sleep(0.5)
pyautogui.keyUp('alt')
time.sleep(0.5)

pyautogui.moveTo(0.5*width, 0.5*height)
pyautogui.mouseDown()
time.sleep(2)

pyautogui.move(0.2*width, -0.2*height)
pyautogui.mouseUp()
time.sleep(2)