
import cv2
import numpy as np 

img = cv2.imread ("outputs\output_1_materwelon.jpg")
img = cv2.resize (img , (326 , 300))
cv2.imshow ("result 4" , img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_1_materwelon.jpg" , img)