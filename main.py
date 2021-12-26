import time

import cv2
import os
from PIL import Image, ImageOps
import numpy
import random

class ImageKernel:

    def __init__(self, image, matrix, kernel):
        #self.img = Image.open(str(image))
        self.out = Image.new("RGB", (450,250), "black")
        self.out = ImageOps.grayscale(self.out)
        self.img = ImageOps.grayscale(image).resize((450,250))
        self.pixel = self.img.load()
        self.width, self.height = self.img.size
        self.kernelSection1 = kernel[0]
        self.kernelSection2 = kernel[1]
        self.kernelSection3 = kernel[2]
        self.matrix = int(matrix)

        self.Run()

    def Run(self):
        for x in range(self.width + 1):
            for y in range(self.height + 1):
                i = x + 1
                k = y + 1
                self.Process((i,k))

    def Process(self, data):
        self.data_x = data[0]
        self.data_y = data[1]

        self.location1 = (self.data_x - 1, self.data_y)
        self.location2 = (self.data_x - 1, self.data_y - 1)
        self.location3 = (self.data_x, self.data_y - 1)
        self.location4 = (self.data_x + 1, self.data_y - 1)
        self.location5 = (self.data_x + 1, self.data_y)
        self.location6 = (self.data_x + 1, self.data_y + 1)
        self.location7 = (self.data_x, self.data_y + 1)
        self.location8 = (self.data_x - 1, self.data_y + 1)
        self.location9 = (self.data_x, self.data_y)

        try:
            self.data_loc1 = int(self.pixel[self.location1] * int(self.kernelSection1[1]))
            self.data_loc2 = int(self.pixel[self.location2] * int(self.kernelSection1[0]))
            self.data_loc3 = int(self.pixel[self.location3] * int(self.kernelSection2[0]))
            self.data_loc4 = int(self.pixel[self.location4] * int(self.kernelSection3[0]))
            self.data_loc5 = int(self.pixel[self.location5] * int(self.kernelSection3[1]))
            self.data_loc6 = int(self.pixel[self.location6] * int(self.kernelSection3[2]))
            self.data_loc7 = int(self.pixel[self.location7] * int(self.kernelSection2[2]))
            self.data_loc8 = int(self.pixel[self.location8] * int(self.kernelSection1[2]))
            self.data_loc9 = int(self.pixel[self.location9] * int(self.kernelSection2[1]))

            count = int(self.data_loc1 + self.data_loc2 + self.data_loc3 +
                        self.data_loc4 + self.data_loc5 + self.data_loc6 +
                        self.data_loc7 + self.data_loc8 + self.data_loc9)

            count = int(count / 9)

            LOCATION_LIST = [
                             self.location1, self.location2, self.location3,
                             self.location4, self.location5, self.location6,
                             self.location7, self.location8,
                             ]

            for lt in LOCATION_LIST:
                if(self.pixel[self.location9] - self.pixel[lt] > 50):
                    self.out.putpixel(
                        lt,
                        (255)
                    )

        except:
            pass


    def show(self):
        return [self.img, self.out]



cam = cv2.VideoCapture("car2.mp4")

while (True):

    ret, frame = cam.read()
    PIL_image = Image.fromarray(frame)
    objects = ImageKernel(PIL_image, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    PIL_image_array = objects.show()[0].convert("RGB")
    PIL_image_cv = numpy.array(PIL_image_array)
    PIL_c = PIL_image_cv[:, :, ::-1].copy()

    PIL_image_array2_out = objects.show()[1].convert("RGB")
    PIL_image_cv_out = numpy.array(PIL_image_array2_out)
    PIL_c2 = PIL_image_cv_out[:, :, ::-1].copy()

    cv2.imshow("PIL_c1", PIL_c)
    cv2.imshow("PIL_c2", PIL_c2)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()