
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_1_watermelon.jpg")
img = cv2.resize (img , (650 , 500))

img_rgb = cv2.cvtColor (img , cv2.COLOR_RGB2BGR)
img_hsv = cv2.cvtColor (img_rgb , cv2.COLOR_RGB2HSV)

h , s , v = cv2.split (img_hsv)
h = h.astype (np.float32)

for i in range (img.shape[0]) :
    for j in range (img.shape[1]) :
        
        if 25 < h [i , j] < 80 :
            h [i , j] -= 42
        
            if h [i , j] < 0 :
                h [i , j] += 180
        
        elif h [i , j] < 15 or h [i , j] > 165 :
            h [i , j] += 60
            v [i , j] -= 10

h = h.astype (np.uint8)

result = cv2.merge ((h , s , v))
result = cv2.cvtColor (result , cv2.COLOR_HSV2BGR)

cv2.imshow ("result 1" , result)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_1_materwelon.jpg" , result)