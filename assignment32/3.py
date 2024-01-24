
import cv2
import numpy as np 

def noise_canceling (input , output) :

    img = cv2.imread (input)
    result = cv2.medianBlur (img , 3)
    cv2.imwrite (output , result)

noise_canceling ("inputs\input_3_xray.png" , "outputs\output_3_xray.jpg")
noise_canceling ("inputs\input_3_board.png" , "outputs\output_3_board.jpg")
noise_canceling ("inputs\input_3_image.png" , "outputs\output_3_image.jpg")
noise_canceling ("inputs\input_3_balloones.png" , "outputs\output_3_balloones.jpg")
noise_canceling ("inputs\input_3_laidy.png" , "outputs\output_3_laidy.jpg")
noise_canceling ("inputs\input_3_a.png" , "outputs\output_3_a.jpg")