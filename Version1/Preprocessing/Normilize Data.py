"""
* By M.K
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

FileCount = int(input('Count>>> '))
Name = r"E:\NFS Train Files\Data-Part{}.npy"
NoMatchCount = 0

TrainData = None

Lefts = []
Rights = []
Forwards = []
"""
Reverses = []
FL = []                       # Forward Left
FR = []                       # Forward Right
RL = []                       # Reverse Left
RR = []                       # Reverse Right
Stops = []                     # No key is pressed
"""
# ====================================================
for i in range(1, FileCount+1):
    print("Working on file number{}".format(i))
    TrainData = np.load(Name.format(i), allow_pickle=True)
    shuffle(TrainData)

    for data in TrainData:
        Image = cv2.cvtColor(data[0], cv2.COLOR_BGR2GRAY)
        Image = Image/255
        Choice = data[1]

        if Choice == [0, 1, 0]:
            Forwards.append([Image, 1])

        elif Choice == [1, 0, 0]:
            Lefts.append([Image, 2])

        elif Choice == [0, 0, 1]:
            Rights.append([Image, 3])

        else:
            NoMatchCount += 1
        """
        elif Choice == [0, 0, 0, 1]:
            Reverses.append([Image, 4])
    
        elif Choice == [1, 1, 0, 0]:
            FL.append([Image, 5])
    
        elif Choice == [0, 1, 1, 0]:
            FR.append([Image, 6])
    
        elif Choice == [1, 0, 0, 1]:
            RL.append([Image, 7])
    
        elif Choice == [0, 0, 1, 1]:
            RR.append([Image, 8])
    
        elif Choice == [0, 0, 0, 0]:
            Stops.append([Image, 9])
        """
    print("File number {} closed.".format(i))


Forwards = Forwards[:len(Lefts)][:len(Rights)]
Lefts = Lefts[:len(Forwards)]
Rights = Rights[:len(Lefts)]
"""
Reverses = Reverses[:len(Rights)]
FL = Reverses[:len(Reverses)]
FR = Reverses[:len(FL)]
RL = Reverses[:len(FR)]
RR = Reverses[:len(RL)]
Stops = Reverses[:len(RR)]
"""
FinalData = Forwards + Lefts + Rights
shuffle(FinalData)

# =================================================
np.save('Final-Data-Merged.npy', FinalData)

print('Process completed! \n Find no Matches for {} images.\n Fianl Data Len = {}'.format(NoMatchCount, len(FinalData)))

# END
