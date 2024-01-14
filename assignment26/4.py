
import cv2

img_white = cv2.imread ("4_input.jpg")

for row in range (120 , 220) :
    for col in range (145 , 175) :
        img_white[row][col] = 0

for row in range (90 , 120) :
    for col in range (110 , 210) :
        img_white[row][col] = 0

cv2.imshow ("result 4" , img_white)
cv2.waitKey ()
cv2.imwrite ("4_output.jpg" , img_white)