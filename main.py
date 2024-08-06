import time

import pyautogui

SIDEWALK_TIME = 0.3
SPARK_POWDER = (1381, 371)
GUN_POWDER = (1566, 370)
PULL_BUTTON = (1440, 36)


def walk():
    pyautogui.keyDown('w')
    time.sleep(SIDEWALK_TIME)
    pyautogui.keyUp('w')


def access_remote_inv():
    pyautogui.keyDown('f')
    time.sleep(1)
    pyautogui.keyUp('f')


def craft():
    pyautogui.click(SPARK_POWDER)
    time.sleep(0.2)
    pyautogui.click(PULL_BUTTON)
    time.sleep(0.2)
    for _ in range(10):
        pyautogui.keyDown('a')
        time.sleep(0.2)
        pyautogui.keyUp('a')


def main():
    for _ in range(4):
        access_remote_inv()
        craft()
        walk()


if __name__ == '__main__':
    main()
