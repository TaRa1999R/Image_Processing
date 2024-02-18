
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_4_rubik.png")

b , g , r = cv2.split (img)

for i in range (img.shape [0]) :
    for j in range (img.shape [1]) :
        if b [i , j] == g [i , j] != r [i , j] :
            b [i , j] = 0
            g [i , j] = 0
            r [i , j] = 255
        
        elif b [i , j] == r [i , j] != g [i , j] :
            b [i , j] = 0
            r [i , j] = 0
            g [i , j] = 255
        
        elif g [i , j] == r [i , j] != b [i , j] :
            g [i , j] = 0
            r [i , j] = 0
            b [i , j] = 255

result = cv2.merge ([b , g ,r])

cv2.imshow ("result 4" , result)
cv2.waitKey ()
cv2.imwrite ("outputs\output_4_rubik.jpg" , result)