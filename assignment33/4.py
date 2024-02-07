
import cv2
import numpy as np

def mine_contourArea (contour) :
    x_list = contour [ : , : , 0]
    y_list = contour [ : , : , 1]
    n = len (contour)
    
    area = 0
    j = n - 1

    for i in range (n) :
        area += (x_list [j] + x_list [i]) * (y_list [j] - y_list [i])
        j = i

    return area [0] / 2.0


img = cv2.imread ("inputs\input_BW.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (img , 120 , 255 , cv2.THRESH_BINARY)
contours , _ = cv2.findContours (thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

for contour in contours :
    # cv2
    area = cv2.contourArea (contour)
    print (area)

    # mine
    area = mine_contourArea (contour)
    print (area)
