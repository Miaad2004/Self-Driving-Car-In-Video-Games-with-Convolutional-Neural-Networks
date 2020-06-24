import numpy as np
from PIL import ImageGrab
import cv2
import time


class Processing:
    def __init__(self):
        self.Vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]])

    def roi(self, image):
        mask = np.zeros_like(image)
        cv2.fillPoly(mask, [self.Vertices], 255)
        masked = cv2.bitwise_and(image, mask)
        return masked

    def detect_lines(self, image):
        try:
            lines = cv2.HoughLinesP(image, 1, np.pi/180, 180, np.array([]), 100, 5)
            for line in lines:
                coords = line[0]
                cv2.line(image, (coords[0], coords[1]), (coords[2], coords[3]), (255, 255, 255), 3)

        except:
            pass

    def main(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        processed = cv2.Canny(image, 200, 300)
        processed = self.roi(processed)
        processed = cv2.GaussianBlur(processed, (5, 5), 0)
        self.detect_lines(processed)
        return processed


processing = Processing()


LastTime = time.time()
while True:
    Image = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    cv2.imshow('main', processing.main(Image))

    print("Loop takes {} seconds".format(time.time() - LastTime))
    LastTime = time.time()

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
