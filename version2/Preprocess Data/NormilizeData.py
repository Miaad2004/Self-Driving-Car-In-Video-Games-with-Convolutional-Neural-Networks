"""
* By M.K
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import cv2
import numpy as np
import time
from random import shuffle

InputAddress = r"D:\ML\NFS Train files\Version 3\parts-not normalized\TrainFiles-part {}.npy"
OutputAddress = r"D:\ML\NFS Train files\Version 3\Normalized Parts\{}-Normalized- Part {}.npy"
FileName = r"Normalized-Data"                    # For saving
TestSplitSize = 0.06


class Preprocessing(object):
    def __init__(self, test_split, data_dir, crop_height):
        self.Data = []
        self.TestSplit = test_split                   # TestData size
        self.Height = crop_height                     # For cropping image
        self.Address = data_dir                       # For loading data

        self.forwards = []
        self.lefts = []
        self.rights = []

        self.FinalData = []
        self.x_train = []
        self.y_train = []
        self.x_test = []
        self.y_test = []

    def load_data(self, part_numbers):               # loading all data parts
        for i in range(1, part_numbers + 1):
            print("Loading part {}".format(i))
            file = np.load(self.Address.format(i), allow_pickle=True)

            for row in file:
                self.Data.append(row)

        shuffle(self.Data)
        print("Input data length = {}".format(len(self.Data)))

    def norm_targets(self):        # Normalizing labels
        counter = 0
        
        for row in self.Data:
            counter += 1
            if counter % 100 == 0 :
                print(counter)

            # ================
            image = row[0]
            image = self.norm_image(image)
            choice = row[1]

            if choice[0] == 1:
                self.lefts.append([image, [1, 0, 0]])

            elif choice[2] == 1:
                self.rights.append([image, [0, 0, 1]])

            elif choice[1] == 1:
                self.forwards.append([image, [0, 1, 0]])
            
        del self.Data             # free uping ram

    def norm_image(self, image):
        image = image[self.Height:, :]

        r, g, b = cv2.split(image)
        r, g, b = r/255, g/255, b/255

        image = cv2.merge((r, g, b))
        return image

    def norm_length(self):           # All classes shouls have same length
        self.forwards = self.forwards[: len(self.lefts)][: len(self.rights)]
        self.lefts = self.lefts[: len(self.forwards)]
        self.rights = self.rights[: len(self.lefts)]

        self.FinalData = self.rights + self.lefts + self.forwards
        shuffle(self.FinalData)      # shuffling final data
        
    def split_data(self):            
        test_data_length = len(self.FinalData) * self.TestSplit

        images = []
        targets = []

        for row in self.FinalData:
            images.append(row[0])
            targets.append(row[1])

        print(targets)

        self.x_train = images[: int(len(self.FinalData) - test_data_length)]
        self.y_train = targets[: int(len(self.FinalData) - test_data_length)]

        self.x_test = images[int(len(self.FinalData) - test_data_length):]
        self.y_test = targets[int(len(self.FinalData) - test_data_length):]

        print("Lengths >>> NormalizedData = {}".format(len(self.FinalData)))
        print("Lengths >>> x_train = {}\ty_train = {}".format(len(self.x_train), len(self.y_train)))
        print("Lengths >>> x_test = {}\ty_test={}".format(len(self.x_test), len(self.y_test)))

        self.x_train, self.y_train = np.array(self.x_train), np.array(self.y_train)   # Converting to np array
        self.x_test, self.y_test = np.array(self.x_test), np.array(self.y_test)

        print("Shapes >>> x_train = {}, y_train = {}".format(self.x_train.shape, self.y_train.shape))
        print("Shapes >>> x_test = {}, y_test = {}".format(self.x_test.shape, self.y_test.shape))


    def save_data(self, address, split_part_number=6):         # saving data in multiple parts
        print("Saving...")
        train_data_length = int(len(self.y_train))

        train_split_file_length = int(train_data_length / split_part_number)     

        counter = 0
        for i in range(1, split_part_number + 1):
            print("Working on part {}.".format(i))

            if i == split_part_number:                                          # If processing last part
                x_train = self.x_train[train_split_file_length * counter:]
                y_train = self.y_train[train_split_file_length * counter:]

            else:
                x_train = self.x_train[train_split_file_length * counter: train_split_file_length * (counter + 1)]
                y_train = self.y_train[train_split_file_length * counter: train_split_file_length * (counter + 1)]

            print("File number {} length =\t{}\n".format(i, len(y_train)))
            np.save(address.format("X-Train", i), x_train)
            np.save(address.format("Y-Train", i), y_train)

            counter += 1

        np.save(address.format("X-Test", 0), self.x_test)
        np.save(address.format("Y-Test", 0), self.y_test)
        print(type(self.y_test), self.y_test)
        print("Done Saving!")


preprocessing = Preprocessing(TestSplitSize, InputAddress, 115)


def main():
    input_part_numbers = int(input("How Many Parts To Load >>> "))
    output_part_numbers = int(input("Split file to how many parts >>> "))

    preprocessing.load_data(input_part_numbers)
    print("Normalizing...")
    preprocessing.norm_targets()
    print("Length Normalizing")
    preprocessing.norm_length()
    print("Split Data")
    preprocessing.split_data()
    print("Saving Data")
    preprocessing.save_data(OutputAddress, output_part_numbers)

    print("Done!")


if __name__ == '__main__':
    main()

# END