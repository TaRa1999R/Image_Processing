
import cv2

cap = cv2.VideoCapture (0)
writer = cv2.VideoWriter ("assignment27\outputs\output_4.mp4" , cv2.VideoWriter_fourcc(*'mpv4') , 10 , (640 , 480))

while True :
    _ , fram = cap.read ()
    fram = cv2.cvtColor (fram , cv2.COLOR_BGR2GRAY)
    # print (fram.shape)      -->   (480 , 640)
    cv2.rectangle (fram , (260 , 180) , (380 , 300) , (255 , 255 , 255) , 2)
    check_color = fram[179:302 , 259:382]
    blur_fram = cv2.blur (fram, (30 , 30))
    blur_fram[179:302 , 259:382] = check_color
    
    for row in range (205 , 265) :
        for col in range (290 , 350) :
            if blur_fram[row , col] >= 200 :
                cv2.putText (blur_fram , "WHITE" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))

            elif blur_fram[row , col] <= 50 :
                cv2.putText (blur_fram , "BLACK" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (255 , 255 , 255))

            else :
                cv2.putText (blur_fram , "GRAY" , (180 , 150) , cv2.FONT_HERSHEY_COMPLEX , 3 , (0 , 0 , 0))


    cv2.imshow ("result 4" , blur_fram)
    writer.write (blur_fram)
    if cv2.waitKey (100) & 0xFF == ord ('q') :
        break

cap.release ()
writer.release ()
# cv2.destroyAllWindows()  
