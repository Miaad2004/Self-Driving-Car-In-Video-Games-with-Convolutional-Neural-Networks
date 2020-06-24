"""
* https://github.com/MI-K253/Python-Plays-Game
"""

from PIL import ImageGrab
from numpy import array
import cv2


def get():
    image = array(ImageGrab.grab(bbox=(0, 50, 1280, 1024)))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

# END