"""
* By M.K 
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import KeyboardControl
import GetFrame
import time
import cv2
from tensorflow import keras
import numpy as np
import MotionDetection
import threading
import keyboard


ImageWeight = 224
ImageHeight = 224

Classes = {0: 'Forward', 1: 'Left', 2: 'Right'}         # , 3: 'Reverse', 4: 'FL', 5: 'FR', 6: 'RL', 7: 'RF', 8: 'Stop'}

KeyboardDelay = 0.1
MaxSpeed = 40
ReverseDelay = 1                                          # For motion detection & high speed
MotionThreshold = 1000

CountdownNumber = 5
CountdownDelay = 0.5

Model = keras.models.load_model(r"Trained-Models/Trained-Alexnet-64.h5")


def keyboard_handler(result, delay):

    if result == 0:
        KeyboardControl.left(delay*1.2)

    elif result == 1:
        KeyboardControl.straight(delay)

    elif result == 2:
        KeyboardControl.right(delay*1.2)


def countdown(num, delay):
    for i in list(range(num))[::-1]:
        if i == 0:
            print("Start driving!")
            continue
        print(i)
        time.sleep(delay)


def main():
    countdown(CountdownNumber, CountdownDelay)
    motion_detected = True

    while True:
        if not motion_detected:
            KeyboardControl.reverse(3)

        start_time = time.time()

        frame = GetFrame.get()

        motion_detected = True

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, (ImageWeight, ImageHeight))

        frame = np.array(frame)
        frame = frame.reshape(1, ImageHeight, ImageWeight, 1)
        frame = frame/255

        prediction = Model.predict(frame)
        prediction = np.argmax(prediction)
        keyboard_handler(prediction, KeyboardDelay)

        print(f"Chice= {prediction}\tProcess took {str(time.time() - start_time)[0: 4]} seconds.")


if __name__ == '__main__':
    main()

# END