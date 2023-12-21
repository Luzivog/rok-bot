from utils import *
from config import *

window = getWindow('BlueStacks -')
if not window:
    print("No such window found")
    exit()


gathering_count = 0
while 1:

    if AUTO_TRAIN:

        for i in range(4):
            if sum(getPixelColorWindow(window, *TRAINING_COORDS[i])) >= 660:
                clickInWindow(window, *CLICK_TRAINING_COORDS[i])
                randomWaitTime(1.0, 2.5)
                clickInWindow(window, *CLICK_TRAINING_COORDS[i])
                randomWaitTime(1.0, 2.5)
                clickInWindow(window, CLICK_TRAINING_COORDS[i][0]+190, CLICK_TRAINING_COORDS[i][1]+197)
                randomWaitTime(1.0, 2.5)
                clickInWindow(window, 1434, 862)
                print(getTime()+"Trained", ["Infantry", "Siege", "Archers", "Cavalry"][i])
                randomWaitTime(1.0, 2.5)

        if AUTO_HELP:
            if sum(getPixelColorWindow(window, 1764, 722)) > 660:
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
            count = 0
            for i in range (len(EXPLORE_COORDS)):
                if getPixelColorWindow(window, *EXPLORE_COORDS[i]) == (255, 175, 0):
                    count += 1
                    print(getTime()+"Sending scout", i+1, "to explore")
                    clickInWindow(window, *EXPLORE_COORDS[i])
                    waitPixelColorWindow(window, 1069, 699, (255, 176, 0))
                    randomWaitTime(2.0, 4.0)
                    clickInWindow(window, 1069, 699)
                    randomWaitTime(1.5, 2.5)
                    clickInWindow(window, 1742, 157+178*i)
                    randomWaitTime(1.0, 2.0)
                    clickInWindow(window, 1352, 263+178*i)
                    randomWaitTime(1.0, 2.0)
                    pyautogui.press('space')
                    waitSumPixelColorWindow(window, 120, 771, 660)
                    randomWaitTime(1.0, 2.0)
                    if i+1 != len(EXPLORE_COORDS):
                        clickInWindow(window, 695, 710)
                        randomWaitTime(1.0, 2.5)
                        clickInWindow(window, 880, 886)
                        randomWaitTime(1.0, 2.5)

            if count == 0:
                pyautogui.press('esc')
                randomWaitTime(1.0, 2.5)

        if AUTO_GATHER and randint(0,6) == 0:
            inactiveMarchesCount = inactiveMarches(window)
            if inactiveMarchesCount == 0: continue

            print(getTime()+f"Inactive march{'es' if inactiveMarchesCount > 1 else ''} detected, sending...")
            pyautogui.press('space')
            waitPixelColorWindow(window, 120, 773, (31, 107, 152))
            randomWaitTime(0.5, 1.5)

            node_found = False
            while not node_found:
                for i in range(inactiveMarchesCount):
                    pyautogui.press('f')
                    waitPixelColorWindow(window, 393, 827, (253, 249, 202))
                    randomWaitTime(0.5, 1.5)

                    if gathering_count < len(GATHERING_QUEUE):
                        rss_type = GATHERING_QUEUE[gathering_count]
                    else: 
                        rss_type = RSS_COORDS.keys()[randint(0, len(RSS_COORDS)-1)]
                        print(getTime()+"Gathering queue empty, random rss type selected:", rss_type)
                    clickInWindow(window, *RSS_COORDS[rss_type])

                    randomWaitTime(1.5, 2.5)
                    clickInWindow(window, RSS_COORDS[rss_type][0], RSS_COORDS[rss_type][1]-200)
                    sleep(3.0)
                    if getPixelColorWindow(window, 938, 497) == (14, 154, 0):
                        print(getTime()+"RSS node already exploited, getting another one")
                    else:
                        node_found = True
                    randomWaitTime(1.0, 2.0)

                    clickInWindow(window, 942, 531)
                    waitPixelColorWindow(window, 1392, 708, (0, 197, 255))
                    randomWaitTime(0.5, 1.5)
                    clickInWindow(window, 1392, 708)
                    waitPixelColorWindow(window, 1461, 238, (0, 195, 255))
                    randomWaitTime(0.5, 1.5)
                    clickInWindow(window, 1461, 238)
                    waitPixelColorWindow(window, 1595, 319, (27, 150, 207))
                    randomWaitTime(0.5, 1.5)
                    for i in range(NUMBER_OF_MARCHES):
                        clickInWindow(window, 1595, 319+77*i)
                        randomWaitTime(0.5, 1.0)

                    randomWaitTime(1.0, 2.0)
                    clickInWindow(window, 1351, 923)
                    print(getTime()+f"March{'es' if inactiveMarchesCount > 1 else ''} sent to RSS node")
                    gathering_count += 1
                    if gathering_count < len(GATHERING_QUEUE): print(getTime()+"Remaining gathering queue", GATHERING_QUEUE[gathering_count:])
                    else: print(getTime()+"Gathering queue empty, now gathering random rss")
                    randomWaitTime(1.5, 2.5)

                pyautogui.press('space')
                waitSumPixelColorWindow(window, 120, 771, 660)
                randomWaitTime(1.0, 2.0)

    randomWaitTime(1.5, 4.0)