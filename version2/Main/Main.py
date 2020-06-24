"""
* By M.K 6/24/2020
* Licensed under the MIT License.
* https://github.com/MI-K253
* https://github.com/MI-K253/Python-Plays-Game
"""

import GetFrame
import numpy as np
from tensorflow import keras
import time
import cv2
import keyboard
from random import randint
import os
import threading
import MotionDetecter
import winsound
from playsound import playsound


class Driver(object):                         # Main class
    def __init__(self):
        keras.backend.learning_phase_scope(0)
        self.Max_Speed = 45
        self.Keyboard_Delay = 0.1             # Delay between press and release
        self.Turn_Threshold = 2.23
        self.Motion_Threshold = 300_000
        # ======================
        self.Speed = None
        self.Paused = False                   
        self.Pause_Key = "p"
        self.Classes = {0: "Left\t", 1: "Straight", 2: "Right   "}          # labels
        self.Speed_Control_Model = keras.models.load_model(os.path.join("Models", "Speed_Controller_V2.h5"))
        self.Main_Model = keras.models.load_model(os.path.join("Models", "mobilenet_v2", "log_ver 0.4-mobilenet_v2-Python-Plays-NFS.h5"))

        self.Thread_2 = threading.Thread(target=self.keyboard_control, args=([], None))
        self.Thread_2.name = "Keyboard_Control_Thread"
        self.Thread_2.start()

        self.Delta_Value = None                  # For Motion detection
        self.Motion_Detection = MotionDetecter.MotionDetection()
        self.Motion_Detection.init(GetFrame.get())

    def motion_detection(self, frame, threshold, speed):
        self.Delta_Value = self.Motion_Detection.main(frame)          

        if speed != 0 and self.Delta_Value > threshold:           # if car isn't stuck 
            return  True

        self.keyboard_control(["w"], 0.3)                         # else we'll try to go forward for 0.3 seconds, if the speed still the same the car is stuck 
        frame = GetFrame.get()                                
        self.Speed = self.get_speed(frame)
        if self.Speed > 8:
            return True

        return False 

    def get_speed(self, image, model=None):
        if model is None:
            model = self.Speed_Control_Model

        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        middle_digit = image[894: 939, 1124: 1166]                # croping image
        middle_digit = cv2.resize(middle_digit, (45, 40))

        right_digit = image[895: 939, 1125 + 41: 1165 + 41]
        right_digit = cv2.resize(right_digit, (45, 40))

        middle_digit, right_digit = np.array(middle_digit, dtype="float32") / 255, np.array(right_digit, dtype="float32") / 255       # Data Normalization
        middle_digit = np.reshape(middle_digit, (1, middle_digit.shape[0], middle_digit.shape[1], 1)),       # (1, width, height, channels)
        right_digit = np.reshape(right_digit, (1, right_digit.shape[0], right_digit.shape[1], 1))

        predictions = (model.predict(middle_digit), model.predict(right_digit))
        speed = np.argmax(predictions[0]) * 10 + np.argmax(predictions[1]) 
        return speed


    @staticmethod
    def make_prediction(frame, model=None):                  # Driver Model
        if model is None:
            model = self.Main_Model

        frame = cv2.resize(frame, (299, 299))                # preprocessing
        frame = frame[115:, :]
        frame = np.array(frame)
        frame = keras.applications.mobilenet_v2.preprocess_input(frame)
        frame = frame.reshape(1, 184, 299, 3)

        predictions = np.argmax(model.predict(frame))
        return predictions

    @staticmethod
    def keyboard_control(keys, delay):
        for key in keys:
            keyboard.press(key)
            time.sleep(delay)
            keyboard.release(keys)

    def main(self):
        if keyboard.is_pressed("p"):
            if self.Paused:
                self.Paused = False        # start driving
                playsound(r"voices/start_driving.mp3")

            else:
                self.Paused = True         # stop driving
                playsound(r"voices/stop_driving.mp3")

                for key in ["a", "w", "d", "s"]:
                    keyboard.release(key)

            time.sleep(1)

        if self.Paused:
            return
        # ====================

        start_time = time.time()
        frame = GetFrame.get()
        self.Speed = self.get_speed(frame)

        prediction = self.make_prediction(frame, self.Main_Model)              # classes --> left , right , straight
        self.Thread_2.join()                                                   # Wait until, all keys are released

        if self.motion_detection(frame, self.Motion_Threshold, self.Speed):
            if prediction == 0:
                if self.Speed >= self.Max_Speed:           # pressing "A"
                    self.Thread_2 = threading.Thread(target=self.keyboard_control, args=(["a"], self.Keyboard_Delay * self.Turn_Threshold))
                    self.Thread_2.start()

                else:                                      # pressing "A" & "W"                              
                    self.Thread_2 = threading.Thread(target=self.keyboard_control, args=(["a", "w"], self.Keyboard_Delay * self.Turn_Threshold))
                    self.Thread_2.start()

            elif prediction == 1:                         
                if self.Speed >= self.Max_Speed:             
                    self.Thread_2 = threading.Thread(target=self.keyboard_control, args=([], self.Keyboard_Delay))
                    self.Thread_2.start()

                else:                                       # pressing "W"
                    self.Thread_2 = threading.Thread(target=self.keyboard_control, args=(["w"], self.Keyboard_Delay))
                    self.Thread_2.start()

            elif prediction == 2:                           # pressing "D"
                if self.Speed >= self.Max_Speed:
                    self.Thread_2 = threading.Thread(target=self.keyboard_control, args=(["d"], self.Keyboard_Delay * self.Turn_Threshold))
                    self.Thread_2.start()

                else:                                       # pressing "D" & "W"
                    self.Thread_2 = threading.Thread(target=self.keyboard_control, args=(["d", "w"], self.Keyboard_Delay * self.Turn_Threshold))
                    self.Thread_2.start()

        else:
            print("No Motion Detected.")
            playsound(r"voices/car_is_stuck.mp3")

            for key in ["a", "w", "s", "s"]:                # releasing all keys
                keyboard.release(key)

            choices = {0: ["s", "a"], 1: ["S", "d"]}
            self.keyboard_control(choices[randint(0, 1)], 0.8)     # random choice
            time.sleep(2)
            self.keyboard_control(["w"], 0.5)                      # going straight for 0.5 seconds

        # ===================          
        frame_rate = 1 / (time.time() - start_time)                
        print(f"Frame rate= {str(frame_rate)[: 5]}  choice= {self.Classes[prediction]}  Speed= {self.Speed}  Delta= {self.Delta_Value}")   # printing logs
        print(f"Active-Thrads= {threading.active_count()} \t Process Took {str(time.time() - start_time)[: 3]} seconds.")

# =============================================
driver = Driver()

if __name__ == '__main__':
    
    for i in list(range(1, 10))[::-1]:
        if i > 3:                        # Beeping (before driving)
            print(i)
            winsound.Beep(2800, 250)
            time.sleep(0.5)
            continue

        winsound.Beep(2800, 1000)
        time.sleep(0.1) 

        if i == 1:
            print("Start Driving...")
            playsound(r"voices/start_driving.mp3")
            driver.keyboard_control(["w"], 2.5)
    
    while True:                          # Main loop
        try:
            driver.main()

        except Exception as e:

            for key in ["w", "a", "s", "d"]:
                keyboard.release(key)

            raise 
# END