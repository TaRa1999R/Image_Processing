
import cv2

img_white = cv2.imread ("assignment26\inputs\input_4.jpg")

for row in range (120 , 220) :
    for col in range (145 , 175) :
        img_white[row][col] = 0

for row in range (90 , 120) :
    for col in range (110 , 210) :
        img_white[row][col] = 0

cv2.imshow ("result 4" , img_white)
cv2.waitKey ()
cv2.imwrite ("assignment26\outputs\output_4.jpg" , img_white)