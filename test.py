from twocaptcha import TwoCaptcha
import pygetwindow
import pyautogui
import cv2
import numpy as np
from utils import *
from config import *
from time import sleep
import random
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

windows = pygetwindow.getWindowsWithTitle('BlueStacks -')

if len(windows) == 0:
    print("No such window found")
    exit()

window = windows[0]
window.activate()

waitSumPixelColorWindow(window, 120, 771, 660)
print("hoi")