
import cv2

img_white = cv2.imread ("assignment26\inputs\input_5.jpg")
color = 255
change = 1
for row in range (510) :
    for col in range (510) :
        img_white[row][col] = color
    change += 1
    if change == 3 :
        color -= 1
        change = 1

cv2.imshow ("result 5" , img_white)
cv2.waitKey ()
cv2.imwrite ("assignment26\outputs\output_5.jpg" , img_white)