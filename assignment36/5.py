
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_5_superman.jpg")
img = cv2.resize (img , (1100 , 750))


cv2.imshow ("result 5" , img)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_5_superman.jpg" , img)