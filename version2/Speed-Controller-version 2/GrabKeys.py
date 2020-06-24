"""
* https://github.com/MI-K253/Python-Plays-Game
"""

import keyboard


def get():
    key_list = []
    if keyboard.is_pressed('a'):
        key_list.append('a')

    if keyboard.is_pressed('w'):
        key_list.append('w')

    if keyboard.is_pressed('d'):
        key_list.append('d')

    if keyboard.is_pressed('s'):
        key_list.append('s')

    if keyboard.is_pressed('t'):
        key_list.append('t')

    if keyboard.is_pressed('y'):
        key_list.append('y')

    return key_list

# END
