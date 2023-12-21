import pygetwindow
from utils import *
import time

windows = pygetwindow.getWindowsWithTitle('BlueStacks -')

if len(windows) == 0:
    print("No such window found")
    exit()

window = windows[0]

while 1:
    coords = getMouseCoordsWindow(window)
    print(coords)
    print(getPixelColorWindow(window, coords[0], coords[1]))
    time.sleep(3)