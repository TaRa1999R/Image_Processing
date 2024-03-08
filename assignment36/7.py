
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_7_spiderman.jpeg")
img = cv2.resize (img , (500 , 750))

img_rgb = cv2.cvtColor (img , cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor (img_rgb , cv2.COLOR_RGB2HSV)

h , s , v = cv2.split (img_hsv)

for i in range (h.shape [0]) :
    for j in range (h.shape [1]) :
        if h [i , j] < 20 or h [i , j] > 170 :
          h [i , j] += 20


result = cv2.merge ((h , s , v))
result = cv2.cvtColor (result , cv2.COLOR_HSV2RGB)

cv2.imshow ("result 7" , img)
cv2.waitKey ()
cv2.imshow ("result 7" , result)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_7_spiderman_new_outfit.jpg" , img)