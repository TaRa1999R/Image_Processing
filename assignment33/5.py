
import cv2
import numpy as np

def check_white (row , col) :
    ...


def mine_findContours (img) :
    m_contours = []
    for row in range (img.shape[0]) :
        for col in range (img.shape[1] - 1 , -1 , -1) :
            if img[row][col] == 255 :
                contours = []
                new = []
                white = [col , row]
                new.append (white)
                contours.append (new)
                print (f'[{col} {row}]')
                break


image = cv2.imread ("inputs\input_1_BW_1.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (image , 170 , 255 , cv2.THRESH_BINARY)

# open cv code
# contours , _ = cv2.findContours (thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)

#my code
# contours = mine_findContours (thresh)