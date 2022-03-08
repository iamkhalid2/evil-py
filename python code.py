import time
import pyautogui
time.sleep(5)
for x in range(200):
    pyautogui.typewrite("Your message here")
    pyautogui.press('enter')