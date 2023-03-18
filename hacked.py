import os
import time
import pyautogui
import subprocess
import threading
subprocess.Popen('notepad.exe')
time.sleep(1)

def hibernate(delay):
    def delayed_hibernate():
        time.sleep(delay)
        os.system("shutdown /h")
    threading.Thread(target=delayed_hibernate).start()

hibernate(3)
while True:
    subprocess.Popen('notepad.exe')
    pyautogui.write('HACKED YOU :-)')
    pyautogui.press('enter')

