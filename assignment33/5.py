
import cv2
import numpy as np

def check_below () : ...


def check_left () : ...


def check_right () : ...


def mine_findContours (image) :
    
    for row in range (image.shape[0]) :
        for col in range (image.shape[1]) :
            if image[row][col] == 255 :
                print (f'[{col} {row}]')
                break
                
    
img = cv2.imread ("inputs\input_BW.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (img , 120 , 255 , cv2.THRESH_BINARY)
# cv2.imshow ("" , thresh)
# cv2.waitKey ()

# cv2 code
contours , _ = cv2.findContours (thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
x,y,w,h = cv2.boundingRect (contours[0])
cv2.rectangle (img , (x,y) , (x+w,y+h) , (255,0,0) , 3)
cv2.imshow ("" , img)
cv2.waitKey ()
print (contours [0])

# mine code
# my_contours = mine_findContours (thresh , )
# print (my_contours [0])
