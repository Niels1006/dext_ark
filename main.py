import time

import pyautogui


# SIDEWALK_TIME = 1
#
#
# def walk():
#     pyautogui.keyDown('w')
#     time.sleep(SIDEWALK_TIME)
#     pyautogui.keyUp('w')
#
# def access_remote_inv():
#     pyautogui.keyDown('f')
#     time.sleep(1)
#     pyautogui.keyUp('f')
#
#
# if __name__ == '__main__':
#     walk()

def place():
    pyautogui.click(100, 100)
    pyautogui.click(100, 100)


def main():
    pyautogui.keyDown('s')

    for _ in range(100):
        place()

    pyautogui.keyUp('s')


if __name__ == '__main__':
    time.sleep(10)
    main()
