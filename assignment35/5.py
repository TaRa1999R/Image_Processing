
import cv2
import numpy as np 

def encrypt (img , key) :
    img_np = np.array (img)
    key_np = np.array (key)

    result = np.bitwise_xor (img_np , key_np)
    return result

image = cv2.imread ("inputs\input_5_Mona_Lisa.jpg")
key = np.random.randint (0 , 256 , image.shape , np.uint8)

encrypt_img = encrypt (image , key)

cv2.imshow ("result 5 : Encrypt Image" , encrypt_img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_5_encryption.jpg" , encrypt_img)

# cv2.imshow ("result 5" , ...)
# cv2.waitKey ()
# cv2.imwrite ("outputs\output_5_dencryption.jpg" , ...)