"""
* https://github.com/MI-K253/Python-Plays-Game
"""

import cv2
import numpy as np
from time import sleep

print("Loading Data...")
Datas = np.load(r"D:\ML\NFS Train files\Final-Data-Merged-Encoded.npy", allow_pickle=True)

for i in list(range(5))[::-1]:
    print(i)
    sleep(0.8)


Counter = 0
#print(Datas["images"][0])
while Counter <= len(Datas):
    Counter += 1
    cv2.imshow("DataSet", Datas[Counter][0])
    print(Datas[Counter][1])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


