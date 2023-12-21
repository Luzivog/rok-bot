from twocaptcha import TwoCaptcha
import pygetwindow
import pyautogui
import cv2
import numpy as np
from utils import *
from config import *
import time
import random

windows = pygetwindow.getWindowsWithTitle('BlueStacks -')

if len(windows) == 0:
    print("No such window found")
    exit()

window = windows[0]
window.activate()

