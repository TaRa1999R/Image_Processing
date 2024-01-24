
import cv2
import numpy as np 

def filtering (img , size , amount) :
    kernel = np.ones ((size , size)) / amount
    result = cv2.filter2D (img , -1 , kernel)
    return result


img = cv2.imread ("inputs\input_2.tif")
img_5_4 = filtering (img , 5 , 25)
img_5_1 = filtering (img , 5 , 1)
img_5_5 = filtering (img , 5 , 1/5)
img_3_4 = filtering (img , 3 , 25)
img_3_1 = filtering (img , 3 , 1)
img_3_5 = filtering (img , 3 , 1/5)

result = np.hstack ((img , img_5_4 , img_5_1 , img_5_5 , img_3_4 , img_3_1 , img_3_5))

cv2.imwrite ("outputs\output_2_magic.jpg" , result)