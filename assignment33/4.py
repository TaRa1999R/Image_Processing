
import cv2
import numpy as np

def mine_contourArea (contour) :
    print (contour)
    print (len (contour))
    x_1 = contour[0][0][0]
    y_1 = contour[0][0][1]
    area = 0

    return area

    

img = cv2.imread ("inputs\input_BW.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (img , 120 , 255 , cv2.THRESH_BINARY)
contours , _ = cv2.findContours (thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

# for contour in contours :
    # cv2
area = cv2.contourArea (contours[0])
print (area)

    # mine
    # area = mine_contourArea (contour)
    # print (area)

are = mine_contourArea (contours[0])
