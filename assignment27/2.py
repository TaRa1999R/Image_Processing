
import cv2
import numpy as np

img = cv2.imread ("assignment27\inputs\input_2.jpg")
img = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)
rows , cols = img.shape
writer = cv2.VideoWriter ("assignment27\outputs\output_2.mp4" , cv2.VideoWriter_fourcc(*'mpv4') , 10 , (cols , rows))

while True :
    img_noise = np.random.random ((106 , 126)) * 255
    img_noise = np.array (img_noise , dtype= np.uint8)
    img[142:248 , 237:363] = img_noise

    writer.write (img)
    cv2.imshow ("result 2" , img)
    if cv2.waitKey (25) & 0xFF == ord('q') :
        break

writer.release ()