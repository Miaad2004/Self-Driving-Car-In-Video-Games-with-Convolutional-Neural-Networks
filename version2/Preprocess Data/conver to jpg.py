"""
* By M.K
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import numpy as np
import pandas as pd
import cv2
from tqdm import tqdm
from random import shuffle
import matplotlib.pyplot as plt


class Converter(object):
    def __init__(self):
        self.Part_Number = int(input("Enter Part number >>> "))                   # geting data part number
        self.Input_Address = r"D:/ML/NFS Train files/Version 3/Normalized Parts/Not Compressed/{}-Train-Normalized- Part {}.npy"
        self.Output_Address = r"D:/ML/NFS Train files/Version 3/"
        self.Images = []
        self.Labels = []
        self.Ids = []
        self.Final_Data = None

    @staticmethod
    def visualize_data(data, title, bins):        

        hist1_y, _, _ = plt.hist(data, bins=bins)       # Data histogram
        plt.title(title)
        plt.yticks(np.arange(0, hist1_y.max(), 3000))

        plt.tight_layout()
        plt.savefig("Python-Plays-NFS-Data-Histogram-HQ.jpg", dpi=1600, quality=100, optimize=True)     # saving figure

    def main(self):
        x = np.load(self.Input_Address.format('X', self.Part_Number), allow_pickle=True)                # loading each data part
        y = np.load(self.Input_Address.format('Y', self.Part_Number), allow_pickle=True)

        for i in tqdm(range(0, len(x))):
            image = x[i] * 255
            image = cv2.cvtColor(np.float32(image), cv2.COLOR_BGR2RGB)
            cv2.imwrite(self.Output_Address + "images/" + str(self.Part_Number) + "/" + str(i) + ".jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 100]) # Save each image

            self.Labels.append(y[i])
            self.Ids.append(i)

        self.visualize_data(self.Labels, "Labels", 3)
        self.Final_Data = {"ID": self.Ids, "Label": self.Labels}
        self.Final_Data = pd.DataFrame(data=self.Final_Data)             # Converting data to pandas Data Frame 

    def save_data(self):
        print("Saving...")
        self.Final_Data.to_pickle(self.Output_Address + "Labels-part{}.pkl".format(self.Part_Number))
        self.Final_Data.to_csv(self.Output_Address + "Labels-part{}.csv".format(self.Part_Number))
        print("Done Saving!")


converter = Converter()

if __name__ == '__main__':
    converter.main()
    converter.save_data()

# END