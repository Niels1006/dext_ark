import os
import sys
import time
import multiprocessing
from threading import Thread

import pyautogui
from PyThreadKiller import PyThreadKiller
from pynput import keyboard
from niels_coloredlogger.logger import logger

CHEM_BENCH_TIME = 0.36
FABRICATOR_TIME = 0.21

SPARK_POWDER = (1289, 371)
GUN_POWDER = (1568, 370)
ARB = (1477, 645)

PULL_BUTTON = (1440, 36)

ITERATIONS = 100


def walk(key, time_):
    pyautogui.keyDown(key)
    time.sleep(time_)
    pyautogui.keyUp(key)


def access_remote_inv():
    pyautogui.press('f')


def close_remote_inv():
    pyautogui.press('esc')


def craft(items):
    for item in items:
        pyautogui.click(item)
        time.sleep(0.2)
        pyautogui.click(PULL_BUTTON)
        time.sleep(0.2)
        pyautogui.click(item)
        time.sleep(0.2)
        for _ in range(10):
            pyautogui.press('a')
            time.sleep(0.1)


def main_():
    for data in [
        {'key': 'a', 'items': [SPARK_POWDER, GUN_POWDER], "iters": 100, "sleep_time": CHEM_BENCH_TIME},
        {'key': 'd', 'items': [ARB], "iters": 83, "sleep_time": FABRICATOR_TIME}
    ]:
        for _ in range(data["iters"]):
            logger.info(f'Accessing remote inventory..')
            access_remote_inv()
            time.sleep(0.6)
            logger.info(f'Crafting items..')
            craft(data['items'])
            time.sleep(0.2)
            logger.info(f'Closing remote inventory..')
            close_remote_inv()
            time.sleep(0.2)
            logger.info(f'Walking..')
            walk(data["key"], data["sleep_time"])
            time.sleep(0.2)

        pyautogui.press('c')
        time.sleep(0.2)


def on_press(key):
    try:
        if key.char == 'q':
            thread.kill()
            logger.info('Thread killed, exiting..')
            sys.exit()
    except AttributeError:
        pass


def test():
    while True:
        print('test')
        time.sleep(0.5)


if __name__ == '__main__':
    logger.info('Starting the script in 5 seconds..')
    logger.info('Press "q" to stop the script..')
    time.sleep(5)

    thread = PyThreadKiller(target=main_)
    thread.start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
