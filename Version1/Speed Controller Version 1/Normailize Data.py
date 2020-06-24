"""
* https://github.com/MI-K253/Python-Plays-Game
"""

import numpy as np
import cv2
from time import sleep

Data = np.load("Speed-Data.npy", allow_pickle=True)
Images = []


counter = 0
FrameNumber = 0
for i in range(0, 100):
    for i in Data:
        if not(counter == 3 or counter == 7):
            Classes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            Classes[FrameNumber] = 1

            frame = cv2.cvtColor(i[0], cv2.COLOR_BGR2GRAY)
            frame = frame[204:218, 196:204]          # Cropping image
            frame = frame / 255

            Images.append([frame, FrameNumber])
            FrameNumber += 1

        counter += 1
    counter = 0
    FrameNumber = 0

Images = np.array(Images)
print(Images)
np.save("Speed-Data-Normilized.npy", Images)

# END