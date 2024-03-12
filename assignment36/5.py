
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_5_superman.jpg")
img = cv2.resize (img , (1100 , 750))

back = cv2.imread ("inputs\input_5_milad_day.jpg")
back = cv2.resize (back , (1100 , 750))


cv2.imshow ("result 5" , back)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_5_superman.jpg" , img)