
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_7_spiderman.jpeg")
img = cv2.resize (img , (500 , 750))


cv2.imshow ("result 7" , img)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_7_spiderman_new_outfit.jpg" , img)