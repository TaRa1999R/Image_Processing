
import cv2
import numpy as np

img = cv2.imread ("inputs\input_1_puppy.jpg" , cv2.IMREAD_GRAYSCALE)



cv2.imshow("" , img)
cv2.waitKey()