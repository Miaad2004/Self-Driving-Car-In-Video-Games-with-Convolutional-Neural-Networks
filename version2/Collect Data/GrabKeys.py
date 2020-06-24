"""
* https://github.com/MI-K253/Python-Plays-Game
"""

import keyboard

def get():
    pressed_keys = []
    if keyboard.is_pressed('a'):
        pressed_keys.append('a')

    if keyboard.is_pressed('w'):
        pressed_keys.append('w')

    if keyboard.is_pressed('d'):
        pressed_keys.append('d')

    if keyboard.is_pressed('s'):
        pressed_keys.append('s')

    if keyboard.is_pressed('t'):
        pressed_keys.append('t')

    if keyboard.is_pressed('y'):
        pressed_keys.append('y')

    return pressed_keys

# END
