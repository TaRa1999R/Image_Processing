
import cv2
import numpy as np 

def encrypt_img (img , key) :
    img_np = np.array (img)

image = cv2.imread ("inputs\input_5_Mona_Lisa.jpg")

cv2.imshow ("result 5" , ...)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_5_encryption.jpg" , ...)

# cv2.imshow ("result 5" , ...)
# cv2.waitKey ()
# cv2.imwrite ("outputs\output_5_dencryption.jpg" , ...)