
import pyautogui as pt
from time import sleep
import cv2
import pyperclip
import random
sleep(3)
img = cv2.imread(r"paperclip2.png")
position1 = pt.locateOnScreen(img, grayscale=True, confidence=.5)
print(position1)

def get_message():
    global x, y

    position = pt.locateOnScreen(img, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 70, y - 40, duration=.5)
get_message()