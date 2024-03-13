
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_6_tara.jpg")
img = cv2.resize (img , (370 , 750))
cv2.imshow ("" , img)
cv2.waitKey ()
cv2.imwrite ("inputs\input_6_tara_resized.jpg" , img)