
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_BW.jpg", cv2.IMREAD_GRAYSCALE)
img_hist = cv2.calcHist ([img] , [0] , None , [256] , [0 , 256])

white = np.ones (img.shape , dtype = np.uint8) * 255
row = 0
col = 0

for color in range (256) :
    for n in range (int (img_hist[color])) :
        if row < img.shape [0] :
            if col < img.shape [1] :
                white [row][col] = color
                # row += 1
                # col += 1
            
            else :
                col = 0
        
        else :
            row = 0
        
        row += 1
        col += 1

cv2.imshow ("" ,img)
cv2.waitKey ()
cv2.imshow ("" ,white)
cv2.waitKey ()
cv2.imwrite ("inputs\input_BW_3.jpg" , white)