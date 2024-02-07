
import cv2
import numpy as np

def mine_findContours (image) :
    contours_list = ...

    return contours_list



img = cv2.imread ("inputs\input_BW.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (img , 120 , 255 , cv2.THRESH_BINARY)

# cv2 code
contours , _ = cv2.findContours (thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
print (contours [0])

# mine code
# my_contours = mine_findContours (thresh)
# print (my_contours [0])
