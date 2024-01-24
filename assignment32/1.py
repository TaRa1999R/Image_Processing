
import cv2
import numpy as np

img = cv2.imread ("inputs\input_1_puppy.jpg")

kernel_edge = np.array ([[-1 , -1 , -1] ,
                         [-1 , 8 , -1] ,
                         [-1 , -1 , -1]])

kernel_sharpening = np.array ([[0 , -1 , 0] , 
                               [-1 , 5 , -1] ,
                               [0 , -1 , 0]])

kernel_emboss = np.array ([[-2 , -1 , 0] , 
                           [-1 , 1 , 1] ,
                           [0 , 1 , 2]])

kernel_identity = np.array ([[0 , 0 , 0] ,
                             [0 , 1 , 0] ,
                             [0 , 0 , 0]])

kernel_horizental = np.array ([[-2 , -2 , -2] ,
                               [0 , 0 , 0] ,
                               [2 , 2 , 2]])

edge_detection = cv2.filter2D (img , 0 , kernel_edge)
sharpening = cv2.filter2D (img , 0 , kernel_sharpening)
emboss = cv2.filter2D (img , 0 , kernel_emboss)
identity = cv2.filter2D (img , 0 , kernel_identity)
horizental = cv2.filter2D (img , 0 , kernel_horizental)

result = np.hstack ((img , edge_detection , sharpening , emboss , identity , horizental))

cv2.imwrite ("outputs\output_1_2Dfilter.jpg" , result)