
import cv2
import numpy as np 

def filtering (img , filter) :
    rows , cols = img.shape
    new_img = np.ones ((rows , cols) , dtype = np.uint8)

    for i in range (1 , rows - 1) :
        for j in range (1 , cols - 1) :
            small = img [i - 1 : i + 2 , j - 1 : j + 2]
            new_img [i , j] = np.abs (np.sum (filter * small))
    
    return new_img


img_bulding = cv2.imread ("inputs\input_4_bilding.png" , cv2.IMREAD_GRAYSCALE)

filter_horizental = np.array ([[-1 , -1 , -1] ,
                               [0 , 0 , 0] ,
                               [1 , 1 , 1]])

filter_vertical = np .array ([[1 , 0 , -1] , 
                              [1 , 0 , -1] , 
                              [1 , 0 , -1]])

horizental = filtering (img_bulding , filter_horizental)
vertical = filtering (img_bulding , filter_vertical)

cv2.imwrite ("outputs\output_4_horizental.jpg" , horizental)
cv2.imwrite ("outputs\output_4_vertical.jpg" , vertical)