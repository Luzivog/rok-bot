from mss import mss
from PIL import Image
from time import sleep, strftime, localtime
from pygetwindow import getWindowsWithTitle
from random import randint, uniform
import pyautogui
from config import *
from twocaptcha import TwoCaptcha
import pytesseract

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def activateWindow(window):
    if not window.isActive: window.activate()

def capture_screenshot(window):
    activateWindow(window)
    [left, top], [right, bottom] = window.topleft, window.bottomright
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab({"top": top, "left": left, "width": right-left, "height": bottom-top})
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

def capture_screenshot_region(window, x1, y1, x2, y2):
    activateWindow(window)
    [left, top], [right, bottom] = window.topleft, window.bottomright
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab({"top": top + y1, "left": left + x1, "height": y2-y1, "width": x2-x1})
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

def clickInWindow(window, x, y, mouseDown=False):
    activateWindow(window)
    [left, top], [right, bottom] = window.topleft, window.bottomright
    pyautogui.click(left + x, top + y)

def moveInWindow(window, x, y):
    activateWindow(window)
    [left, top], [right, bottom] = window.topleft, window.bottomright
    pyautogui.moveTo(left + x, top + y)

def getPixelColorWindow(window, x, y):
    activateWindow(window)
    [left, top], [right, bottom] = window.topleft, window.bottomright
    return pyautogui.pixel(left + x, top + y)

def getMouseCoordsWindow(window):
    activateWindow(window)
    [left, top], [right, bottom] = window.topleft, window.bottomright
    x, y = pyautogui.position()
    return (x - left, y - top)

def waitPixelColorWindow(window, x, y, color):
    activateWindow(window)
    [left, top], [right, bottom] = window.topleft, window.bottomright
    while not pyautogui.pixelMatchesColor(left + x, top + y, color, tolerance=10):
        sleep(0.2)

def waitSumPixelColorWindow(window, x, y, total):
    activateWindow(window)
    [left, top], [right, bottom] = window.topleft, window.bottomright
    while sum(getPixelColorWindow(window, x, y)) < total:
        sleep(0.2)

def solve_captcha(window):
    clickInWindow(window, 1539, 193)
    waitPixelColorWindow(window, 1187, 548, (7, 193, 251))
    randomWaitTime(0.5, 1.0)
    clickInWindow(window, 1187, 548)
    waitPixelColorWindow(window, 666, 181, (255, 255, 255))
    randomWaitTime(0.5, 1.0)
    
    count = 0
    sleep(2.5)
    while getPixelColorWindow(window, 1056, 854) == (186, 217, 255):

        if count > 0: # Refresh captcha if fail
            clickInWindow(window, 776, 852)
            sleep(3.0)

        captcha_region = (657, 170, 1226, 899)
        capture_screenshot_region(window, *captcha_region).save("captcha.jpg")
        sleep(3.0)

        print(getTime()+"Screenshoted captcha, sending to 2captcha...")

        solver = TwoCaptcha(API_KEY)
        result = solver.coordinates('./captcha.jpg')

        print(getTime()+"Received result from 2captcha, inputting...")

        if not result.get('code'):
            print('<!> Failed to solve captcha <!>')
            print("<!> Result:", result)
        else:
            coordinates = result.get('code')[12:].split(';')
            for c in coordinates:
                x, y = list(map(lambda x: int(x[2:]), c.split(',')))
                clickInWindow(window, captcha_region[0] + x, captcha_region[1] + y)
                randomWaitTime(0.5, 1.0)
                moveInWindow(window, randint(captcha_region[0], captcha_region[2]),randint(captcha_region[1], captcha_region[3]))
                randomWaitTime(0.5, 1.0)
            clickInWindow(window, 1116, 857)
            sleep(4.0)
            count += 1

    return solver.balance()

def randomWaitTime(min, max):
    return sleep(uniform(min, max))

def getWindow(window_name):
    windows = getWindowsWithTitle(window_name)
    if len(windows) == 0:
        return False
    return windows[0]

def getTime():
    return strftime("[%H:%M:%S] ", localtime())

def inactiveMarches(window):
    capture_screenshot_region(window, 1746, 260, 1780, 280).save("marches.jpg")
    sleep(1.0)
    text = pytesseract.image_to_string("marches.jpg", lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    if len(text) == 0: return NUMBER_OF_MARCHES
    else: return NUMBER_OF_MARCHES - int(text[0])