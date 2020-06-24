"""
* By M.K
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import numpy as np
import os
import sys
import cv2
from tqdm import tqdm
from keras.utils import to_categorical
np.set_printoptions(threshold=sys.maxsize)

Images_Dir = r"Data/{}.jpg"
Image_Count = 11

def main():
	images = []
	labels = []

	for i in tqdm(range(0, Image_Count)):
		image = cv2.imread(Images_Dir.format(i), 0)

		if i == 0:
			image = cv2.resize(image, (45, 40))
			print(np.shape(image))
			continue

		image = image[895: 940, 1125: 1165] 
		image = cv2.resize(image, (45, 40))
		print(np.shape(image))

		cv2.imshow(f"image{i}.jpg", image)
		cv2.waitKey()


		image = np.array(image) / 255
		images.append(image)
		label = int(input(f"Enter image {i} label >>> "))            # Manually labeling data
		labels.append(label)

	images, labels = images * 100, labels * 100                      # Duplicating images
	images = np.array(images)
	labels = to_categorical(np.array(labels))
	print(f"Shape:\tX: {images.shape}  Y: {labels.shape}\n")

	print("Saving..")
	np.save("Data/X.npy", images)         # Save data
	np.save("Data/Y.npy", labels)
	print("Done")

	return 0

if __name__ == "__main__":
	main()
	_ = input("Press any key to exit >>> ")

# END