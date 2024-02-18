
import cv2
import numpy as np 

rows = 686
cols = 1156

white = np.ones ((rows , cols , 3) , dtype = np.uint8) * 255

cv2.ellipse (white , (600 , cols // 2) , (380 , 380) , 180 , 0 , 180 , (68 , 16 , 245) , 30)           # red 
cv2.ellipse (white , (600 , cols // 2) , (350 , 350) , 180 , 0 , 180 , (64 , 128 , 255) , 30)          # orange
cv2.ellipse (white , (600 , cols // 2) , (320 , 320) , 180 , 0 , 180 , (1 , 228 , 254) , 30)           # yello
cv2.ellipse (white , (600 , cols // 2) , (290 , 290) , 180 , 0 , 180 , (0 , 221 , 0) , 30)             # green
cv2.ellipse (white , (600 , cols // 2) , (260 , 260) , 180 , 0 , 180 , (232 , 162 , 0) , 30)           # blue
cv2.ellipse (white , (600 , cols // 2) , (230 , 230) , 180 , 0 , 180 , (255 , 113 , 194) , 30)           # indigo
cv2.ellipse (white , (600 , cols // 2) , (200 , 200) , 180 , 0 , 180 , (174 , 74 , 134) , 30)          # violet

my_rainbow = white [0 : 580 , :]

cv2.imshow ("result 2" , my_rainbow)
cv2.waitKey ()
cv2.imwrite ("outputs\output_2_rainbow.jpg" , my_rainbow)