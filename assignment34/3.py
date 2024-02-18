
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_3_watermelon.jpg")
img = cv2.resize (img , (1000 , 700))

b , g , r = cv2.split (img)

for i in range (g.shape [0]) :
    for j in range (g.shape [1]) :
        if 100 < g [i , j] < 200 :
            g [i , j] += 50

result = cv2.merge ([b , r , g])

cv2.imshow ("result 3" , result)
cv2.waitKey ()
cv2.imwrite ("outputs\output_3_watermelon.jpg" , result)