import pyautogui
from time import sleep


SPEED = 20
screenWidth, screenHeight = pyautogui.size()
x_increment, y_increment = 1, 1
pyautogui.FAILSAFE = False

while True:
    x, y = pyautogui.position()

    # glitch in the library, don't pay attention to this
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    if x == 0 or x == screenWidth:
        x_increment *= -1
    if y == 0 or y == screenHeight:
        y_increment *= -1

    x, y = x + x_increment, y + y_increment
    pyautogui.moveTo(x, y, duration=1/SPEED, _pause=False)
