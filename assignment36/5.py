
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_5_superman.jpg")
img = cv2.resize (img , (1100 , 750))

background = cv2.imread ("inputs\input_5_milad_day.jpg")
background = cv2.resize (background , (1100 , 750))

s_rgb = cv2.cvtColor (img , cv2.COLOR_BGR2RGB)
s_hsv = cv2.cvtColor (s_rgb , cv2.COLOR_RGB2HSV)
h , _ , _ = cv2.split (s_hsv)

bg_rgb = cv2.cvtColor (background , cv2.COLOR_BGR2RGB)
bg_hsv = cv2.cvtColor (bg_rgb , cv2.COLOR_RGB2HSV)

for i in range (img.shape[0]) :
    for j in range (img.shape[1]) :
        if 31 < h [i , j] < 83 :
            img [i , j] = background [i , j]

cv2.imshow ("result 5" , img)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_5_superman.jpg" , img)