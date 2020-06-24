"""
* By M.K 
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import KeyboardControl
import GetFrame
import keyboard
import numpy as np
import os
import time
import cv2

FileName = r"Speed-Data.npy"
TrainingData = None


def keys_to_output(pressed_keys):
    output = [0, 0, 0]             # A, W, D,

    if 'A' in pressed_keys:
        output[0] = 1

    elif 'D' in pressed_keys:
        output[2] = 1

    else:
        output[1] = 1

    return output


def main():
    for i in list(range(10))[::-1]:
        print(i)
        time.sleep(1)

    if os.path.isfile(FileName):
        print("File Exist, loading data")
        TrainingData = list(np.load(FileName, allow_pickle=True))

    else:
        print("File doesn't exist, making file...")
        TrainingData = []

    last_time = time.time()

    while True:
        if keyboard.is_pressed('t'):
            screen = GetFrame.get()
            screen = cv2.resize(screen, (224, 224))
            keys = keys_to_output(KeyboardControl.key_check())
            TrainingData.append([screen])

            print("Getting data took {} seconds.".format(time.time() - last_time))
            last_time = time.time()

        if keyboard.is_pressed('r'):
            print("Saving!")
            print(len(TrainingData))
            np.save(FileName, TrainingData)
            break


if __name__ == '__main__':
    try:
        main()

    except :
        print("Saving!")
        print(len(TrainingData))
        np.save(FileName, TrainingData)

# END