
import cv2
import numpy as np

# mine version of cv2.boundingRect () code
def mine_bondingRect (contour) :
    x_low = x_high = contour[0][0][0]
    y_low = y_high = contour[0][0][1]
    for c in contour :
        if c[0][0] < x_low :
            x_low = c[0][0]

        if c[0][0] > x_high :
            x_high = c[0][0]

        if c[0][1] < y_low :
            y_low = c[0][1]

        if c[0][1] > y_high :
            y_high = c[0][1]

    x = x_low
    y = y_low
    w = x_high - x_low + 1 
    h = y_high - y_low + 1

    return (x , y , w , h)


img = cv2.imread ("inputs\input_BW.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (img , 120 , 255 , cv2.THRESH_BINARY)
contours , _ = cv2.findContours (thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

for contour in contours :
    x , y , w , h = mine_bondingRect (contour)
    cv2.rectangle (img , (x , y) , (x+w , y+h) , (255 , 0 , 0) , 3)

cv2.imshow ("result" , img)
cv2.waitKey ()