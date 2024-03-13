
import cv2
import numpy as np 

cap = cv2.VideoCapture (0)
writer = cv2.VideoWriter ("outputs\output_4_skin_detector.mp4" , cv2.VideoWriter_fourcc (*'mpv4') , 10 , (640 , 480))

while True :
    _ , frm = cap.read ()

    cv2.imshow ("result 4" , frm)
    writer.write (frm)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break

writer.release ()