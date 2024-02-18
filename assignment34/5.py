
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_5_microsoft_logo.png")

cv2.imshow ("result 5" , img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_5_microsoft_logo.jpg" , img)