
import cv2
import numpy as np 

cap = cv2.VideoCapture (0)
writer = cv2.VideoWriter ("outputs\output_2_color_detector.mp4" , cv2.VideoWriter_fourcc (*'mpv4') , 10 , (640 , 480))

while True :
    _ , frm = cap.read ()

    cv2.rectangle (frm , (260 , 180) , (380 , 300) , (170 , 170 , 170) , 2)

    check_color = frm [179:302 , 259:382]
    blur_frm = cv2.blur (frm , (200 , 200))

    rgb_color = cv2.cvtColor (check_color , cv2.COLOR_BGR2RGB)
    hsv_color = cv2.cvtColor (rgb_color , cv2.COLOR_RGB2HSV)

    h , s , v = cv2.split (hsv_color)
    
    if v [61 , 61] < 20 :                      #black
        cv2.putText (blur_frm , "BLACK" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (200 , 200 , 200))

    elif s [61 , 61] < 20 :                      #white
        cv2.putText (blur_frm , "WHITE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))

    elif h [61 , 61] < 10 or h [61 , 61] > 170 :                      #red
        cv2.putText (blur_frm , "RED" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))

    elif 130 < h [61 , 61] < 145 :                      #purple
        cv2.putText (blur_frm , "PURPLE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))

    elif 83 < h [61 , 61] < 130 :                      #blue
        cv2.putText (blur_frm , "BLUE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))

    elif 31 < h [61 , 61] < 83 :                      #green
        cv2.putText (blur_frm , "GREEN" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))

    elif 29 < h [61 , 61] < 31 :                      #yellow
        cv2.putText (blur_frm , "YELLOW" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))

    elif 10 < h [61 , 61] < 29 :                      #orange
        cv2.putText (blur_frm , "ORANGE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))

    else :
        cv2.putText (blur_frm , "UNKNOWN" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (10 , 10 , 10))
          
    check_color = cv2.merge ((h , s , v))
    check_color = cv2.cvtColor (check_color , cv2.COLOR_HSV2BGR)
    blur_frm [179:302 , 259:382] = check_color

    cv2.imshow ("result 2" , blur_frm)
    writer.write (blur_frm)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break

writer.release ()