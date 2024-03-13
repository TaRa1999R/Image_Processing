
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_6_tara.jpg")
img = cv2.resize (img , (370 , 750))

img_rgb = cv2.cvtColor (img , cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor (img_rgb , cv2.COLOR_RGB2HSV)

h , s , v = cv2.split (img_hsv)
h = h.astype (np.float32)

for i in range (img.shape[0]) :
    for j in range (img.shape[1]) :
        if h [i , j] < 10 or h [i , j] > 110 :                        
            if s [i , j] > 160 and v [i , j] > 50 :
                h [i , j] -= 35

h = h.astype (np.uint8)

result = cv2.merge ([h , s , v])
result = cv2.cvtColor (result , cv2.COLOR_HSV2BGR)

cv2.imshow ("result 6" , result)
cv2.waitKey ()
cv2.imwrite ("outputs\output_6_new_shirt.jpg" , result)