
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_2_rainbow.png")
rows = 686
cols = 1156

r_rainbow = np.zeros ((rows , cols) , dtype = np.uint8) 
g_rainbow = np.zeros ((rows , cols) , dtype = np.uint8) 
b_rainbow = np.zeros ((rows , cols) , dtype = np.uint8) 

# red
cv2.ellipse (r_rainbow , (600 , cols // 2) , (200 , 200) , 180 , 0 , 180 , 145 , 30)
cv2.ellipse (r_rainbow , (600 , cols // 2) , (230 , 230) , 180 , 0 , 180 , 22 , 30)
cv2.ellipse (r_rainbow , (600 , cols // 2) , (260 , 260) , 180 , 0 , 180 , 36 , 30)
cv2.ellipse (r_rainbow , (600 , cols // 2) , (290 , 290) , 180 , 0 , 180 , 72 , 30)
cv2.ellipse (r_rainbow , (600 , cols // 2) , (320 , 320) , 180 , 0 , 180 , 240 , 30)
cv2.ellipse (r_rainbow , (600 , cols // 2) , (350 , 350) , 180 , 0 , 180 , 245 , 30)
cv2.ellipse (r_rainbow , (600 , cols // 2) , (380 , 380) , 180 , 0 , 180 , 237 , 30)

# green
cv2.ellipse (g_rainbow , (600 , cols // 2) , (200 , 200) , 180 , 0 , 180 , 39 , 30)
cv2.ellipse (g_rainbow , (600 , cols // 2) , (230 , 230) , 180 , 0 , 180 , 67 , 30)
cv2.ellipse (g_rainbow , (600 , cols // 2) , (260 , 260) , 180 , 0 , 180 , 242 , 30)
cv2.ellipse (g_rainbow , (600 , cols // 2) , (290 , 290) , 180 , 0 , 180 , 163 , 30)
cv2.ellipse (g_rainbow , (600 , cols // 2) , (320 , 320) , 180 , 0 , 180 , 236 , 30)
cv2.ellipse (g_rainbow , (600 , cols // 2) , (350 , 350) , 180 , 0 , 180 , 148 , 30)
cv2.ellipse (g_rainbow , (600 , cols // 2) , (380 , 380) , 180 , 0 , 180 , 63 , 30)

# blue
cv2.ellipse (b_rainbow , (600 , cols // 2) , (200 , 200) , 180 , 0 , 180 , 240 , 30)
cv2.ellipse (b_rainbow , (600 , cols // 2) , (230 , 230) , 180 , 0 , 180 , 227 , 30)
cv2.ellipse (b_rainbow , (600 , cols // 2) , (260 , 260) , 180 , 0 , 180 , 242 , 30)
cv2.ellipse (b_rainbow , (600 , cols // 2) , (290 , 290) , 180 , 0 , 180 , 74 , 30)
cv2.ellipse (b_rainbow , (600 , cols // 2) , (320 , 320) , 180 , 0 , 180 , 14 , 30)
cv2.ellipse (b_rainbow , (600 , cols // 2) , (350 , 350) , 180 , 0 , 180 , 13 , 30)
cv2.ellipse (b_rainbow , (600 , cols // 2) , (380 , 380) , 180 , 0 , 180 , 5 , 30)

my_rainbow = cv2.merge ([b_rainbow , g_rainbow , r_rainbow])
# for i in range (rows) :
    # for j in range (cols) :
        # if my_rainbow [i , j] == (0 , 0 , 0) :
            # my_rainbow [i , j] = (255 , 255 , 255)

cv2.imshow ("result 2" , my_rainbow)
cv2.waitKey ()
cv2.imwrite ("outputs\output_2_rainbow.jpg" , my_rainbow)