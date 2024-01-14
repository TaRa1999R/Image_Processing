
import cv2
import numpy as np
import tensorflow as tf
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

def rotate_item (img , landmark_place) :
    mask = np.zeros (img.shape , dtype = np.uint8)
    cv2.drawContours (mask , [landmark_place] , -1 , (255 , 255 , 255) , -1)

    mask = mask // 255
    mask = img * mask

    x , y , w , h = cv2.boundingRect (landmark_place)
    crop_mask = mask [y : y + h , x : x + w]
    crop_mask = cv2.flip (crop_mask , 0)

    for row in range (h) :
        for col in range (w) :
            if crop_mask[row][col][0] == crop_mask[row][col][1] == crop_mask[row][col][2] == 0 :
                crop_mask[row][col] = img [y + row , x + col]

    img [y : y + h , x : x + w] = crop_mask

    return img

fd = UltraLightFaceDetecion ("weights/RFB-320.tflite" , conf_threshold=0.88)
fa = CoordinateAlignmentModel ("weights/coor_2d106.tflite")

my_img = cv2.imread ("inputs\Tara.jpg")
color = (125 , 0 , 0)

boxes, scores = fd.inference (my_img)
for pred in fa.get_landmarks (my_img , boxes):
    # for i , p in enumerate(np.round(pred).astype(np.uint)):                              find mouth and eyes location's index
        # cv2.circle (my_img, tuple(p), 1, color, 1, cv2.LINE_AA)
        # cv2.putText (my_img , str(i) , tuple(p) , cv2.FONT_HERSHEY_PLAIN , 0.65 , color)
    
    lips_landmarks = []
    for i_lip in [52 , 55 , 56 , 53 , 59 , 58 , 61 , 68 , 67 , 71 , 63 , 64] :
        lips_landmarks.append (pred[i_lip])
    lips_landmarks = np.array (lips_landmarks , dtype = int)
    my_img = rotate_item (my_img , lips_landmarks)

    left_eye_landmarks = []
    for i_left in [95 , 94 , 96 , 93 , 91 , 87 , 90 , 89] :
        left_eye_landmarks.append (pred[i_left])
    left_eye_landmarks = np.array (left_eye_landmarks , dtype = int)
    my_img = rotate_item (my_img , left_eye_landmarks)

    right_eye_landmarks = []
    for i_right in [35 , 36 , 33 , 37 , 39 , 42 , 40 , 41] :
        right_eye_landmarks.append (pred[i_right])
    right_eye_landmarks = np.array (right_eye_landmarks , dtype = int)
    my_img = rotate_item (my_img , right_eye_landmarks)

result = cv2.flip (my_img , 0)

cv2.imshow ("Rotate the Photo", result)
cv2.waitKey ()
cv2.imwrite ("outputs\output_2_rotate_the_phone.jpg" , result)