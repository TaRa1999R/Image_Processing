
import cv2

image = cv2.imread ("3_input.jpg")
image = cv2.rotate (image , cv2.ROTATE_180)

cv2.imshow ("result 3" , image)
cv2.waitKey ()
cv2.imwrite ("3_output.jpg" , image)