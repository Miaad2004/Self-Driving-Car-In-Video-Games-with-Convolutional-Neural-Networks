"""
* By M.K
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import cv2
import numpy as np
import GetFrame
import time
import keyboard
import os

Counter = 0

def main():
    global Counter
    if not keyboard.is_pressed("t"):
        return

    start_time = time.time()
    frame = GetFrame.get()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(f"{os.getcwd()}/Data/{Counter}.jpg", frame)       # saving frame 
    Counter += 1
    print(f"Process took {str(time.time() - start_time)[: 4]} seconds!")
    time.sleep(1)


if __name__ == "__main__":
    for i in list(range(0, 10))[: : -1]:
        print(i)
        time.sleep(0.5)
    # ==========

    print("Press 't' to take screenshot.")

    while True:
        main()

        if keyboard.is_pressed("e"):
            _ = input("Press any key to exit >>> ")
            break
# END