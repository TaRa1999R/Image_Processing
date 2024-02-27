import random
import cv2
import numpy as np 

input_list = ["inputs\input_2_black.png" , "inputs\input_2_blue.png" , "inputs\input_2_green.png" , "inputs\input_2_orang.png" , "inputs\input_2_purple.png" , "inputs\input_2_red.png" , "inputs\input_2_white.png" , "inputs\input_2_yellow.png"]

i = random.randint (0 , len (input_list) - 1)
img = cv2.imread (input_list[i])

b , g , r = cv2.split (img)

if b[50 , 50] <= 80 and g[50 , 50] <= 80 and r[50 , 50] <= 80 :
    print ("black")

elif b[50 , 50] >= 245 and g[50 , 50] >= 245 and r[50 , 50] >= 245 :
    print ("white")

elif b[50 , 50] >= 145 and g[50 , 50] <= 165 and r[50 , 50] <= 70 :
    print ("blue")

elif b[50 , 50] <= 100 and g[50 , 50] >= 170 and r[50 , 50] <= 120 :
    print ("green")

elif b[50 , 50] <= 100 and 125 <= g[50 , 50] <= 200 and r[50 , 50] >= 245 :
    print ("orange")

elif b[50 , 50] >= 120 and g[50 , 50] <= 100 and r[50 , 50] >= 90 :
    print ("purple")

elif b[50 , 50] <= 100 and g[50 , 50] <= 100 and r[50 , 50] >= 160 :
    print ("red")

elif b[50 , 50] <= 145 and g[50 , 50] >= 225 and r[50 , 50] >= 225 :
    print ("yellow")



cv2.imshow ("result 2" , img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_2_logo.jpg" , img)