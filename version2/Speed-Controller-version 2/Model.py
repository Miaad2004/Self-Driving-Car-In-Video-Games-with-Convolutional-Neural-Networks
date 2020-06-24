"""
* By M.K
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Conv2D, Dropout, MaxPooling2D, Input, Flatten
from tensorflow.keras.callbacks import TensorBoard
from datetime import datetime
import os

Image_Height, Image_Width = 40, 45
Num_Classes = 10
Epochs, Batch_Size = 15, 32
# TB_LogDir = f"logs/Speed-Controller-{Epochs}epochs-{datetime.now()}"
# TB_CallBack = TensorBoard(log_dir=TB_LogDir, histogram_freq=1)

X = np.array(np.load(r"Data/X.npy", allow_pickle=True))
Y = np.array(np.load(r"Data/Y.npy", allow_pickle=True))
X = np.reshape(X, (X.shape[0], Image_Height, Image_Width, 1))             # Reshaping data  --> (nmber, height, width, channels)
print(f"{X}\n\n{Y}\n\nLengths:\tX: {len(X)}  Y:{len(Y)}\nShapes:\tX: {np.shape(X)}  Y: {np.shape(Y)}\n")

def main():
	model = keras.Sequential()
	model.add(Input(shape=(Image_Height, Image_Width, 1)))

	model.add(Conv2D(32, (3, 3), strides=(1, 1), padding="same", activation="relu"))
	model.add(MaxPooling2D())

	model.add(Flatten())

	model.add(Dense(1024, activation="relu"))
	model.add(Dense(512, activation="relu"))
	model.add(Dropout(0.3))
	model.add(Dense(128, activation="relu"))
	model.add(Dense(Num_Classes, activation="softmax"))

	model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
	model.fit(X, Y, epochs=Epochs, batch_size=Batch_Size, validation_split=0.1, verbose=1)
	model.save(r"Speed_Controller.h5")

	return



if __name__ == "__main__":
	main()

# END
