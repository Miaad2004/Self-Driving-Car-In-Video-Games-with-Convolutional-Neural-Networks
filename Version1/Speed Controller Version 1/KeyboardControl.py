"""
* By M.K 
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

from time import sleep
import keyboard


def straight(delay):
    keyboard.press('w')
    sleep(delay)
    keyboard.release('w')


def reverse(delay):
    keyboard.press('s')
    sleep(delay)
    keyboard.release('s')


def right(delay):
    keyboard.press('w')
    keyboard.press('d')
    sleep(delay)
    keyboard.release('w')
    sleep(delay)
    keyboard.release('d')


def left(delay):
    keyboard.press('w')
    keyboard.press('a')
    sleep(delay)
    keyboard.release('w')
    sleep(delay)
    keyboard.release('a')


def straight_left(delay):
    keyboard.press('w')
    keyboard.press('a')
    sleep(delay)
    keyboard.release('w')
    keyboard.release('a')


def straight_right(delay):
    keyboard.press('w')
    keyboard.press('d')
    sleep(delay)
    keyboard.release('w')
    keyboard.release('d')


def reverse_left(delay):
    keyboard.press('s')
    keyboard.press('a')
    sleep(delay)
    keyboard.release('s')
    keyboard.release('a')


def reverse_right(delay):
    keyboard.press('s')
    keyboard.press('d')
    sleep(delay)
    keyboard.release('s')
    keyboard.release('d')


def key_check():
    key_list = []
    if keyboard.is_pressed('w'):
        key_list.append('W')

    if keyboard.is_pressed('d'):
        key_list.append('D')

    if keyboard.is_pressed('a'):
        key_list.append('A')

    if keyboard.is_pressed('s'):
        key_list.append('S')

    if keyboard.is_pressed('e'):
        key_list.append('E')

    if keyboard.is_pressed('r'):
        key_list.append('R')

    return key_list

# END