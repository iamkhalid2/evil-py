import time
import pyautogui

time.sleep(5) # number of seconds you want to wait before the script starts

while True:
    pyautogui.write('Your message here') 
    pyautogui.press('enter')
    time.sleep(0.1)   # Replace 0.1 with the number of seconds you want to wait between key presses

# Move the cursor to the top left corner of the screen to stop the script (Fail safe)
