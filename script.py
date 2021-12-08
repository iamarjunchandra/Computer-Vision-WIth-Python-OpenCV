import cv2
import numpy as np

image=cv2.imread('/home/arjun/Desktop/Q1/chessboard.png')
image=cv2.resize(image, (256,256), interpolation = cv2.INTER_AREA)

for num1 in range(4):
    for num2 in range(4):
        if num1 % 2:
            if num2 % 2:
                image[0+num1*64:64+num1*64, 0+num2*64:64+num2*64]=(255,255,255)
            else:
                image[0+num1*64:64+num1*64, 0+num2*64:64+num2*64]=(0,0,0)
        else:
            if num2 % 2:
                image[0+num1*64:64+num1*64, 0+num2*64:64+num2*64]=(0,0,0)
            else:
                image[0+num1*64:64+num1*64, 0+num2*64:64+num2*64]=(255,255,255)

cv2.imshow("output",image)
cv2.waitKey(0)
