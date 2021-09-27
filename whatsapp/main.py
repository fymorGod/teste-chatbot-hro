import pyautogui as pt
from time import sleep
import cv2
import pyperclip
import random
sleep(2)
img = cv2.imread(r"paperclip2.png")
img2 = cv2.imread(r"green_dot.png")
position1 = pt.locateOnScreen(img, grayscale=True, confidence=.5)
x = position1[0]
y = position1[1]
def get_message():
    global x, y

    position = pt.locateOnScreen(img, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 70, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print('Message received: ' + whatsapp_message)

    return whatsapp_message

def post_response(message):
    global x, y

    position = pt.locateOnScreen(img, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)

def process_response(message):
    random_no = random.randrange(3)
    if "?" in str(message).lower():
        return "Don't ask me any questions"
    else:
        if random_no == 0:
            return "That's cool"
        elif random_no == 1:
            return "Remember to subscribe to Code"
        else:
            return "i want to eat something"

def check_for_new_message():
    pt.moveTo(x+50, y-35, duration=.5)

    while True:

        try:
            position = pt.locateOnScreen(img2, confidence=.6)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)


        except(Exception):
            print('No new other users')

        if pt.pixelMatchesColor(int(x+50), int(y+35), (255,255,255), tolerance=10):
            print('is_white')
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print('No new messages yet...')
        sleep(5)
check_for_new_message()
