
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_1_microsoft_logo.jpg")

cv2.imshow ("result 1" , img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_1_logo.png" , img)