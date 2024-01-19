
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_2_rose.jpg" , cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur (img , (3 , 3) , 5)

_ , thresh = cv2.threshold (img , 110 , 255 , cv2.THRESH_BINARY)
_ , invert_thresh = cv2.threshold (img , 110 , 255 , cv2.THRESH_BINARY_INV)

thresh = thresh // 255
thresh = img * thresh

invert_thresh = invert_thresh // 255
invert_thresh = img * invert_thresh

invert_thresh = invert_thresh + thresh

cv2.imwrite ("outputs\output_2_rose.jpg" , invert_thresh)