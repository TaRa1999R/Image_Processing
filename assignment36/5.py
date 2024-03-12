
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_5_superman.jpg")
img = cv2.resize (img , (1100 , 750))

background = cv2.imread ("inputs\input_5_milad_day.jpg")
background = cv2.resize (background , (1100 , 750))

s_rgb = cv2.cvtColor (img , cv2.COLOR_BGR2RGB)
s_hsv = cv2.cvtColor (s_rgb , cv2.COLOR_RGB2HSV)

bg_rgb = cv2.cvtColor (background , cv2.COLOR_BGR2RGB)
bg_hsv = cv2.cvtColor (bg_rgb , cv2.COLOR_RGB2HSV)



cv2.imshow ("result 5" , back)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_5_superman.jpg" , img)