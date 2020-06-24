"""
* By M.K 
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import tensorflow as tf
from tensorflow import keras                        # Tensorflow API (make things easier:))
import numpy as np

FileName = r"Speed-Data-Normilized.npy"             # Loading train data

Data = np.load(FileName, allow_pickle=True)
x_train = []
y_train = []

for i in Data:
    x_train.append(i[0])
    y_train.append(i[1])

x_train = np.array(x_train)
y_train = np.array(y_train)

print(x_train)
print(y_train)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(14, 8)),
    keras.layers.Dense(4096, activation="relu"),
    keras.layers.Dense(2048, activation="relu"),
    keras.layers.Dense(1024, activation="relu"),
    keras.layers.Dense(512, activation="relu"),
    keras.layers.Dense(256, activation="relu"),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
    ])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])


model.fit(x_train, y_train, epochs=50)

model.save("speed-model.h5")

# END