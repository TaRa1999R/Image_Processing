
import cv2
import numpy as np 


cap = cv2.VideoCapture (0)
writer = cv2.VideoWriter ("outputs\output_2_color_detector.mp4" , cv2.VideoWriter_fourcc (*'mpv4') , 10 , ( 640 , 480))

while True :
    _, frm = cap.read ()
    # b , g , r = cv2.split (frm)

    # if b[50 , 50] <= 80 and g[50 , 50] <= 80 and r[50 , 50] <= 80 :
        # print ("black")

    # elif b[50 , 50] >= 245 and g[50 , 50] >= 245 and r[50 , 50] >= 245 :
        # print ("white")

    # elif b[50 , 50] >= 145 and g[50 , 50] <= 165 and r[50 , 50] <= 70 :
        # print ("blue")

    # elif b[50 , 50] <= 100 and g[50 , 50] >= 170 and r[50 , 50] <= 120 :
        # print ("green")

    # elif b[50 , 50] <= 100 and 125 <= g[50 , 50] <= 200 and r[50 , 50] >= 245 :
        # print ("orange")

    # elif b[50 , 50] >= 120 and g[50 , 50] <= 100 and r[50 , 50] >= 90 :
        # print ("purple")

    # elif b[50 , 50] <= 100 and g[50 , 50] <= 100 and r[50 , 50] >= 160 :
        # print ("red")

    # elif b[50 , 50] <= 145 and g[50 , 50] >= 225 and r[50 , 50] >= 225 :
        # print ("yellow")

    cv2.imshow ("result 2" , frm)
    writer.write (frm)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break

writer.release ()