
import cv2
import numpy as np

img = cv2.imread ("inputs\input_6_MonaLisa.jpeg" , cv2.IMREAD_GRAYSCALE)
# black = np.zeros ((130 , 120))
cap = cv2.VideoCapture (0)
# write = cv2.VideoWriter ("outputs\output_6_funny_video.mp4" , cv2.VideoWriter_fourcc(*'mpv4') , 10 , (img.shape[1] , img.shape[0]))

while True :
    _ , fram = cap.read ()
    fram_g = cv2.cvtColor (fram , cv2.COLOR_BGR2GRAY)
    # fram_s = cv2.resize (fram_g , (120 , 130))
    fram_s = fram_g [fram.shape[0] // 2 - 65 : fram.shape[0] // 2 + 65 , fram.shape[1] // 2 - 60 : fram.shape[1] // 2 + 60]

    img[350 : 480 , 450 : 570] = fram_s

    cv2.imshow ("Funny Webcam" , img)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break

# img[350:480 , 450:570] = black
# cv2.imshow ("" , img)
# cv2.waitKey ()