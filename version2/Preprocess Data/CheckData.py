"""
* By M.K 
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import cv2
import numpy as np

Dir = r"Y-Test- Normalized-Data.npy"             # Data directory
LoopMode = int(input("Loop Mode? 1/0 >>>\t"))             

print("Loading Data")
Data = np.load(Dir, allow_pickle=True)              # Loading Data
print(Data)

for row in Data:
    print(row[1])
    image = cv2.cvtColor(row, cv2.COLOR_RGB2BGR)
    cv2.imshow('FinalData', image)

    if LoopMode:
        if cv2.waitKey(26) & 0xFF == ord('q'):
            break

    else:
        cv2.waitKey()            # waiting until user press a key
