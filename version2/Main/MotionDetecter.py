"""
* 6/24/2020
* https://stackoverflow.com/questions/40514508/opencv-detect-movement-in-python
"""

import cv2

class MotionDetection(object):
    def __init__(self):
        self.t_minus = None
        self.t = None
        self.t_plus = None
        
    @staticmethod
    def get_difference(t0, t1, t2):
        d1 = cv2.absdiff(t2, t1)
        d2 = cv2.absdiff(t1, t0)
        return cv2.bitwise_and(d1, d2)

    def init(self, frame):
        self.t_minus = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        self.t = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        self.t_plus = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    def main(self, frame):
        difference = cv2.countNonZero(self.get_difference(self.t_minus, self.t, self.t_plus))

        self.t_minus = self.t
        self.t = self.t_plus
        self.t_plus = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        return difference
