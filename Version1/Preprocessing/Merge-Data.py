"""
* By M.K
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import numpy as np
import pandas as pd

Address = r"E:/NFS Train Files/Data-Part{}.npy"
Count = int(input("Enter number of parts >>>(5) "))                  # parts
Name = str(input("Enter output name>>> "))
Data = pd.DataFrame()

for i in range(1, Count+1):
    print("Reading File number {}".format(i))
    file = np.load(Address.format(i), allow_pickle=True)
    file = pd.DataFrame(file)
    print(file.head())
    Data = Data.append(file)
    print("Done Reading File Number{}".format(i))

Data.to_csv(Name)
print("Done!\nSaved CSV File")
