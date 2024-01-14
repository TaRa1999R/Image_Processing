
import cv2
import numpy as np
import tensorflow as tf
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

def resize_filter (img , landmark_place , mask) :
    cv2.drawContours (mask , [landmark_place] , -1 , (255 , 255 , 255) , -1)

    mask = mask // 255
    mask = mask * img

    x , y , w , h = cv2.boundingRect (landmark_place)
    crop_mask = mask [y : y + h , x : x + w]
    big_mask = cv2.resize (crop_mask , (0 , 0) , fx = 2 , fy =  2)

    for row in range (2 * h) :
        for col in range (2 * w) :
            if big_mask[row][col][0] == big_mask[row][col][0] == big_mask[row][col][0] == 0 :
                big_mask[row][col] = img [y - h // 2 + row , x - w // 2 + col]

    if h % 2 == 0 :
        h_high = (3 * h // 2) 
    
    else :
        h_high = (3 * h // 2) + 1
    
    if w % 2 == 0 :
        w_high = (3 * w // 2)
    
    else:
        w_high = (3 * w // 2) + 1
    
    img [y - h // 2 : y + h_high , x - w // 2 : x +  w_high] = big_mask
    
    return img

    
fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

my_img = cv2.imread ("inputs\Tara.jpg")
main_mask = np.zeros (my_img.shape , dtype = np.uint8)
color = (0 , 0 , 150)

boxes, scores = fd.inference (my_img)
for pred in fa.get_landmarks (my_img , boxes) :
    # for i , p in enumerate (np.round(pred).astype(np.uint)) :                             find mouth and eyes location's index
        # cv2.circle (my_img , tuple(p) , 1 , color , 1 , cv2.LINE_AA)
        # cv2.putText (my_img , str(i) , tuple(p) , cv2.FONT_HERSHEY_PLAIN , 0.65 , color)

    lips_landmarks = []
    for i_lip in [52 , 55 , 56 , 53 , 59 , 58 , 61 , 68 , 67 , 71 , 63 , 64] :
        lips_landmarks.append (pred[i_lip])
    lips_landmarks = np.array (lips_landmarks , dtype = int)
    result = resize_filter (my_img , lips_landmarks , main_mask)

    left_eye_landmarks = []
    for i_left in [95 , 94 , 96 , 93 , 91 , 87 , 90 , 89] :
        left_eye_landmarks.append (pred[i_left])
    left_eye_landmarks = np.array (left_eye_landmarks , dtype = int)
    result = resize_filter (my_img , left_eye_landmarks , main_mask)

    right_eye_landmarks = []
    for i_right in [35 , 36 , 33 , 37 , 39 , 42 , 40 , 41] :
        right_eye_landmarks.append (pred[i_right])
    right_eye_landmarks = np.array (right_eye_landmarks , dtype = int)
    result = resize_filter (my_img , right_eye_landmarks , main_mask)

cv2.imshow ("Big Eyes & Lips Filter", result)
cv2.waitKey ()
cv2.imwrite ("outputs\output_4_big_eyes_&_lips_filter.jpg" , result)