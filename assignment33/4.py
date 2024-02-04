
import cv2
import numpy as np

img = cv2.imread ("inputs\input_BW.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (img , 120 , 255 , cv2.THRESH_BINARY)

# cv2 code


# mine code


cv2.imshow ("" , thresh)
cv2.waitKey ()
