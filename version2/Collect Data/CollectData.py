"""
* By M.K
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import numpy as np
import time
import GrabScreen
import GrabKeys
import cv2

SaveAddress = r"D:/ML/NFS Train files/Version 3/"
FileName = "TrainFiles-part {}.npy"

ImageHeight = 1041
ImageWeight = 1279

CuntDownDelay = 0.5

Data = []

PartNumber = int(input("Enter part number>>> "))


def keys_to_output(keys):   
    output = [0, 0, 0, 0]

    if 'a' in keys:
        output[0] = 1

    elif 'd' in keys:
        output[2] = 1

    else:
        output[1] = 1

    if 's' in keys:
        output[3] = 1

    return output


def count_down(delay):
    for a in list(range(1, 11))[:: -1]:
        print(a)
        time.sleep(delay)

        if a == 1:
            print("Starting...")


count_down(CuntDownDelay)

while True:
    StartTime = time.time()

    frame = GrabScreen.get()
    frame = frame[30:ImageHeight, 1:ImageWeight]
    frame = cv2.resize(frame, (299, 299))
    
    PressedKeys = GrabKeys.get()     # cropping the edges
    EncodedKeys = keys_to_output(PressedKeys)

    Data.append([frame, EncodedKeys])

    if 'y' in PressedKeys:           # stopping for a few seconds
        for i in list(range(1, 9))[::-1]:
            print(i)
            time.sleep(1)

    if 't' in PressedKeys:           # Save & exit
        print("Len = {}\t saving...".format(len(Data)))
        np.save(SaveAddress + FileName.format(PartNumber), Data)
        break

    StopTime = time.time()
    print("Process took {} seconds.".format(StopTime - StartTime))         

# END
