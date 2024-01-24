
import cv2
import numpy as np 

def noise_canceling (input , output , color) :
    if color == "gray" :
        img = cv2.imread (input , cv2.IMREAD_GRAYSCALE)
    
    else :
        img = cv2.imread (input)
    
    noise_free = cv2.medianBlur (img , 5)
    result = np.hstack ((img , noise_free))
    cv2.imwrite (output , result)

noise_canceling ("inputs\input_3_xray.png" , "outputs\output_3_xray.jpg" , "gray")
noise_canceling ("inputs\input_3_board.png" , "outputs\output_3_board.jpg" , "gray")
noise_canceling ("inputs\input_3_image.png" , "outputs\output_3_image.jpg" , "gray")
noise_canceling ("inputs\input_3_balloones.png" , "outputs\output_3_balloones.jpg" , "all")
noise_canceling ("inputs\input_3_laidy.png" , "outputs\output_3_laidy.jpg" , "all")
noise_canceling ("inputs\input_3_a.png" , "outputs\output_3_a.jpg" , "gray")