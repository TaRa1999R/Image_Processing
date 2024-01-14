
import cv2

img_white = cv2.imread ("5_input.jpg")
color = 255
change = 1
for row in range (510) :
    for col in range (510) :
        img_white[row][col] = color
    change += 1
    if change == 3 :
        color -= 1
        change = 1
print("end :",color)
cv2.imshow ("result 5" , img_white)
cv2.waitKey ()
cv2.imwrite ("5_output.jpg" , img_white)