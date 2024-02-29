
import cv2
import numpy as np 

def encrypt_decrypt (img , key) :
    img_np = np.array (img)
    key_np = np.array (key)

    result = np.bitwise_xor (img_np , key_np)
    return result

image = cv2.imread ("inputs\input_5_Mona_Lisa.jpg")
key = np.random.randint (0 , 256 , image.shape , np.uint8)

encrypt_img = encrypt_decrypt (image , key)
cv2.imshow ("result 5 : Encrypt Image" , encrypt_img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_5_encrypted_image.jpg" , encrypt_img)

decrypt_img = encrypt_decrypt (encrypt_img , key )
cv2.imshow ("result 5" , decrypt_img)
cv2.waitKey ()
cv2.imwrite ("outputs\output_5_dencrypted_image.jpg" , decrypt_img)