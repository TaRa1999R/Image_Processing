
import cv2

image = cv2.imread ("assignment26\inputs\input_3.jpg")
image = cv2.rotate (image , cv2.ROTATE_180)

cv2.imshow ("result 3" , image)
cv2.waitKey ()
cv2.imwrite ("assignment26\outputs\output_3.jpg" , image)