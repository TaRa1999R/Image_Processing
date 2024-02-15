
import cv2
import numpy as np

def mine_findContours (img) :
    img_copy = np.copy (img)
    # img_copy = 255 - img_copy
    m_contours = []
    for row in range (img.shape[0]) :
        for col in range (img.shape[1]) :
            if img [row , col] == img_copy [row , col] == 255 :
                contour = []
                new = [(col , row)]
                img_copy [row , col] = 0
                while len (new) > 0 :
                    y , x = new.pop ()
                    contour.append ((y , x))
                    for dx , dy in [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0) , (1 , 1) , (1 , -1) , (-1 , 1) , (-1 , -1)] :
                        i = x + dx
                        j = y + dy
                        if 0 < i < img.shape [0] and 0 < j < img.shape [1] :
                            if img [i , j] == img_copy [i , j] == 255 :
                                img_copy[i , j] = 0
                                new.append ((j , i))
                
                m_contours.append (np.array (contour))
    return m_contours
                   

image = cv2.imread ("inputs\input_1_BW_1.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (image , 170 , 255 , cv2.THRESH_BINARY)


# open cv code
contours , _ = cv2.findContours (thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
for c in contours :
    x, y, w, h = cv2.boundingRect (c)
    cv2.rectangle (image , (x,y) , (x+w,y+h) , (0 , 0 , 0) , 3)
cv2.imshow ("cv2 result" , image)
cv2.waitKey ()


#my code
contours = mine_findContours (thresh)
for c in contours :
    x, y, w, h = cv2.boundingRect (contours[5])
    cv2.rectangle (image , (x,y) , (x+w,y+h) , (200 , 200 , 200) , 3)
cv2.imshow ("mine result" , image)
cv2.waitKey ()