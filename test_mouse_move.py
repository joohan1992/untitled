import pyautogui

# 현재 화면의 크기 반환
width, height = pyautogui.size()
print(width, height)

# 현재 마우스 포인터의 위치 반환
x, y = pyautogui.position()
print(x, y)

targ_