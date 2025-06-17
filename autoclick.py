import pyautogui
import time
pos_x = 628
pos_y = 608

while True:
    for i in range(6):
        time.sleep(0.5)
        pyautogui.click(pos_x, pos_y)

    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyUp('s')

    pyautogui.keyDown('w')
    time.sleep(0.5)
    pyautogui.keyUp('w')
    time.sleep(3)