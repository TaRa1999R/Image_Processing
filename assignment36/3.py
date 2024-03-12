
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_3_balloons.jpg")

lower_h = np.array ([160 , 0 , 0])
upper_h = np.array ([180 , 255 , 255])

img_rgb = cv2.cvtColor (img , cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor (img_rgb , cv2.COLOR_RGB2HSV)

mask = cv2.inRange (img_hsv , lower_h , upper_h)


cv2.imshow ("result 3" , result)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_3_Balloon_detection.jpg" , img)