
import cv2
import numpy as np 

def contrast (input , output , type) :
    img = cv2.imread (input , cv2.IMREAD_GRAYSCALE)
    if type == "hist" :
        high = cv2.equalizeHist (img)

    else :
        clahe = cv2.createCLAHE (clipLimit = 5)
        high = clahe.apply (img)
    
    result = np.hstack ((img , high))
    cv2.imwrite (output , result)

contrast ("inputs\input_4_land.jpg" , "outputs\output_4_land.jpg" , "hist")
contrast ("inputs\input_4_city.png" , "outputs\output_4_city.jpg" , "hist")
contrast ("inputs\input_4_room.png" , "outputs\output_4_room.jpg" , "clahe")