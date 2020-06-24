"""
* https://github.com/MI-K253/Python-Plays-Game
"""
from PIL import ImageGrab
from numpy import array


def get():
    image = array(ImageGrab.grab(bbox=(0, 50, 1280, 1024)))
    return image

