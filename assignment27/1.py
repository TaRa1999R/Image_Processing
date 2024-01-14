
import cv2

img = cv2.imread ("assignment27\inputs\input_1.jpg")
img = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)

threshold = 140
_, img_batman = cv2.threshold (img , threshold , 255 , cv2.THRESH_BINARY_INV)
cv2.putText (img_batman , "BATMAN" , (375 , 510) , cv2.FONT_ITALIC , 2 , (255 , 255 , 255))

cv2.imshow ("result 1" , img_batman)
cv2.waitKey ()
cv2.imwrite ("assignment27\outputs\output_1.jpg" , img_batman)