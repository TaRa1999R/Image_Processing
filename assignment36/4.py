
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_5_superman.jpg")
img = cv2.resize (img , (650 , 500))
cv2.imshow ("result 4" , img)
cv2.waitKey ()
cv2.imwrite ("inputs\input_5_superman_resized.jpg" , img)