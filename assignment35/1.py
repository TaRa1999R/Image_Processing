
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_1_microsoft_logo.jpg")
img = cv2.cvtColor (img , cv2.COLOR_BGR2BGRA)

for i in range (img.shape [0]) :
    for j in range (img.shape [1]) :
        if img[i][j][0] == img[i][j][1] == img[i][j][2] == 88 :
            img [i , j , 3] = 200

cv2.imshow ("result 1" , img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_1_logo.png" , img)