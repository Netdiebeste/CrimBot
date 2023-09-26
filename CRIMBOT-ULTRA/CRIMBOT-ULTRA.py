#this is a simple script that locates the "claim allowance" button and auto clicks it. 
#you must make sure the click location is set SPECIFICALLY for you (on the claim allowance button)
#use an app like https://sourceforge.net/projects/mpos/ to find the coordinates and put the x value and y value in is appropriate position

from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('button.png', confidence=0.8) != None:
        pyautogui.click(692, 500), print("ALLOWANCE SUCCESFULLY CLAIMED")
        time.sleep(0.5)
    else:
        print("waiting for allowance")
        time.sleep(0.5),
        

