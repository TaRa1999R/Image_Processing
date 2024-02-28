
import cv2
import numpy as np 


cap = cv2.VideoCapture (0)
writer = cv2.VideoWriter ("outputs\output_2_color_detector.mp4" , cv2.VideoWriter_fourcc (*'mpv4') , 10 , (640 , 480))

while True :
    _ , frm = cap.read ()

    cv2.rectangle (frm , (260 , 180) , (380 , 300) , (170 , 170 , 170) , 2)
    check_color = frm [179:302 , 259:382]
    blur_frm = cv2.blur (frm , (200 , 200))
    blur_frm [179:302 , 259:382] = check_color 

    b , g , r = cv2.split (check_color)

    if b[61 , 61] <= 80 and g[61 , 61] <= 80 and r[61 , 61] <= 80 :                      #black
        cv2.putText (blur_frm , "BLACK" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (200 , 200 , 200))

    elif b[61 , 61] >= 200 and g[61 , 61] >= 200 and r[61 , 61] >= 200 :                 #white
        cv2.putText (blur_frm , "WHITE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (10 , 10 ,10))

    elif b[61 , 61] <= 100 and g[61 , 61] >= 200 and r[61 , 61] >= 200 :                 #yellow
        cv2.putText (blur_frm , "YELLOW" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (10 , 10 , 10))

    elif b[61 , 61] >= 145 and g[61 , 61] <= 165 and r[61 , 61] <= 70 :                  #blue
        cv2.putText (blur_frm , "BLUE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (10 , 10 ,10))

    elif b[61 , 61] >= 50 and g[61 , 61] >= 70 and r[61 , 61] <= 45 :                 #green
        cv2.putText (blur_frm , "GREEN" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (200 , 200 , 200))

    elif b[61 , 61] <= 81 and 88 <= g[61 , 61] <= 165 and r[61 , 61] >= 160 :         #orange
        cv2.putText (blur_frm , "ORANGE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (200 , 200 , 200))

    elif b[61 , 61] >= 120 and g[61 , 61] <= 100 and r[61 , 61] >= 90 :                 #purple
        cv2.putText (blur_frm , "PURPLE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (10 , 10 , 10))

    elif b[61 , 61] <= 100 and g[61 , 61] <= 100 and r[61 , 61] >= 160 :                 #red
        cv2.putText (blur_frm , "RED" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (10 , 10 , 10))

    cv2.imshow ("result 2" , blur_frm)
    writer.write (blur_frm)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break

writer.release ()