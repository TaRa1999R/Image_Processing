
import cv2
import numpy as np

img = cv2.imread ("inputs\input_6_MonaLisa.jpeg" , cv2.IMREAD_GRAYSCALE)
cap = cv2.VideoCapture (0)
writer = cv2.VideoWriter ("outputs\output_6_funny_video.mp4" , cv2.VideoWriter_fourcc(*'mpv4') , 10 , (img.shape[1] , img.shape[0]))

while True :
    _ , fram = cap.read ()
    fram_g = cv2.cvtColor (fram , cv2.COLOR_BGR2GRAY)
    fram_f = cv2.flip (fram_g , 1)
    fram_s = fram_f [fram.shape[0] // 2 - 65 : fram.shape[0] // 2 + 65 , fram.shape[1] // 2 - 60 : fram.shape[1] // 2 + 60]

    img[350 : 480 , 450 : 570] = fram_s

    writer.write (img)
    cv2.imshow ("Funny Webcam" , img)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break

writer.release ()