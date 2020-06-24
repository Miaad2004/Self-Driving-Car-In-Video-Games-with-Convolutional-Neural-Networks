"""
* By M.K 
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import cv2
import KeyboardControl
import time
fgbg = cv2.createBackgroundSubtractorMOG2()
LastReverse = round(time.time())


def detect(frame, min_white):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (600, 600))
    frame = cv2.GaussianBlur(frame, (5, 5), 10)
    fgmask = fgbg.apply(frame)
    white_count = cv2.countNonZero(fgmask)

    print(white_count)

    if white_count < min_white: 
        return False                 # No motion detected

    else:
        return True                  # Motion Detected

# END

