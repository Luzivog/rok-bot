from utils import *
from config import *

window = getWindow('BlueStacks -')
if not window:
    print("No such window found")
    exit()

while 1:

    if AUTO_TRAIN:

        for i in range(4):
            if sum(getPixelColorWindow(window, *TRAINING_COORDS[i])) >= 660:
                clickInWindow(window, *TRAINING_COORDS[i])
                randomWaitTime(1.0, 2.5)
                clickInWindow(window, *TRAINING_COORDS[i])
                randomWaitTime(1.0, 2.5)
                clickInWindow(window, TRAINING_COORDS[i][0]+189, TRAINING_COORDS[i][1]+245)
                randomWaitTime(1.0, 2.5)
                clickInWindow(window, 1434, 862)
                print(getTime()+"Trained", ["Infantry", "Siege", "Archers", "Cavalry"][i])
                randomWaitTime(1.0, 2.5)

        if AUTO_HELP:
            if getPixelColorWindow(window, 1764, 722) == (255, 228, 212):
                clickInWindow(window, 1764, 722)
                print(getTime()+"Clicked alliance helps")
                randomWaitTime(1.0, 2.5)

        if SOLVE_CAPTCHA:
            if getPixelColorWindow(window, 1539, 193) == (236, 195, 112):
                print(getTime()+"Captcha detected, solving...")
                balance = solve_captcha(window)
                if balance:
                    print(getTime()+"Captcha solved, remaining balance:", balance)
                randomWaitTime(1.0, 2.5)


        if AUTO_FOG and randint(0, 3) == 0:
            clickInWindow(window, 695, 710)
            randomWaitTime(1.0, 2.5)
            clickInWindow(window, 880, 886)
            randomWaitTime(1.0, 2.5)
            for i in range (len(EXPLORE_COORDS)):
                if getPixelColorWindow(window, *EXPLORE_COORDS[i]) == (255, 175, 0):
                    print(getTime()+"Sending scout", i+1, "to explore")
                    clickInWindow(window, *EXPLORE_COORDS[i])
                    waitPixelColorWindow(window, 1069, 699, (255, 176, 0))
                    randomWaitTime(1.0, 2.0)
                    clickInWindow(window, 1069, 699)
                    waitPixelColorWindow(window, 1352, 263+178*i, (255, 175, 0))
                    randomWaitTime(1.0, 2.0)
                    clickInWindow(window, 1352, 263+178*i)
                    randomWaitTime(1.0, 2.0)
                    pyautogui.press('space')
                    waitPixelColorWindow(window, 120, 771, (234, 255, 255))
                    randomWaitTime(1.0, 2.0)
                    clickInWindow(window, 695, 710)
                    randomWaitTime(1.0, 2.5)
                    clickInWindow(window, 880, 886)
                    randomWaitTime(1.0, 2.5)
            pyautogui.press('esc')

    randomWaitTime(1.5, 4.0)