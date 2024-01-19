
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_2_rose.jpg" , cv2.IMREAD_GRAYSCALE)


cv2.imshow ("" , img)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_2_rose.jpg" , ...)