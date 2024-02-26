
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_1_microsoft_logo.jpg")

# log

cv2.imshow ("result 4" , img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_1_logo.jpg" , img)