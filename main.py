import time

import pyautogui

CHEM_BENCH_TIME = 0.37
FABRICATOR_TIME = 0.25

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


def main():
    for data in [
        {'key': 'a', 'items': [SPARK_POWDER, GUN_POWDER], "iters": 10, "sleep_time": CHEM_BENCH_TIME},
        {'key': 'd', 'items': [ARB], "iters": 8, "sleep_time": FABRICATOR_TIME}
    ]:
        for _ in range(data["iters"]):
            access_remote_inv()
            time.sleep(0.6)
            craft(data['items'])
            time.sleep(0.2)
            close_remote_inv()
            time.sleep(0.2)
            walk(data["key"], data["sleep_time"])
            time.sleep(0.2)

        pyautogui.press('c')
        time.sleep(0.2)


if __name__ == '__main__':
    time.sleep(5)
    main()
