"""
* By M.K 
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

from tensorflow import keras
import KeyboardControl
import cv2
import GetFrame
from time import sleep
import numpy as np

for i in list(range(0, 3))[::-1]:          # count down
    print(i)
    sleep(0.6)

ModelName = r"Speed-model.h5"
MaxSpeed = 40 / 10
delay = 1                                  # for breaking

Model = keras.models.load_model(ModelName)


def main():
    while True:

        image = GetFrame.get()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (224, 224))
        image = image/255

        image = image[204:218, 196:204]
        image = np.array(image)
        image = image.reshape(1, image.shape[0], image.shape[1])

        prediction = Model.predict(image)

        if int(np.argmax(prediction)) > MaxSpeed or int(np.argmax(prediction)) == 0:
            print("High Speed Detected! OR U are stuck!")
            KeyboardControl.reverse(delay)

# END