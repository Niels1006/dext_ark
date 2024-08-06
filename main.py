import time

import pyautogui

SIDEWALK_TIME = 0.15
SPARK_POWDER = (1381, 371)
GUN_POWDER = (1566, 370)
PULL_BUTTON = (1440, 36)

ITERATIONS = 100


def walk():
    pyautogui.keyDown('a')
    time.sleep(SIDEWALK_TIME)
    pyautogui.keyUp('a')


def access_remote_inv():
    pyautogui.press('f')


def close_remote_inv():
    pyautogui.press('esc')


def craft():
    for item in [SPARK_POWDER, GUN_POWDER]:
        pyautogui.click(item)
        time.sleep(0.2)
        pyautogui.click(PULL_BUTTON)
        time.sleep(0.2)
        pyautogui.click(item)
        time.sleep(0.2)
        for _ in range(10):
            pyautogui.press('a')
            time.sleep(0.1)


def main():
    for _ in range(ITERATIONS):
        access_remote_inv()
        time.sleep(0.5)
        craft()
        time.sleep(0.2)
        close_remote_inv()
        time.sleep(0.2)
        walk()


if __name__ == '__main__':
    time.sleep(5)
    main()
