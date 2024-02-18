
import cv2
import numpy as np 

rows = 310
cols = 766

logo = np.ones ((rows , cols , 3) , dtype = np.uint8) * 88

cv2.rectangle (logo , (103 , 103) , (152 , 152) , (34 , 80 , 242) , -1)
cv2.rectangle (logo , (157 , 103) , (206 , 152) , (0 , 186 , 127) , -1)
cv2.rectangle (logo , (103 , 157) , (152 , 206) , (239 , 164 , 0) , -1)
cv2.rectangle (logo , (157 , 157) , (206 , 206) , (0 , 185 , 255) , -1)

cv2.putText (logo , "Microsoft" , (236 , 185) , cv2.FONT_HERSHEY_SIMPLEX , 3 , (255 , 255 , 255) , 10)

cv2.imshow ("result 5" , logo)
cv2.waitKey ()
cv2.imwrite ("outputs\output_5_microsoft_logo.jpg" , logo) 