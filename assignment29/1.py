
import cv2
import numpy as np 

first_photo = cv2.imread ("inputs\input_1_hatmaker.jpeg")
second_photo = cv2.imread ("inputs\input_1_JSparrow.jpeg")

first_gray = cv2.cvtColor (first_photo , cv2.COLOR_BGR2GRAY)
second_gray = cv2.cvtColor (second_photo , cv2.COLOR_BGR2GRAY)

first = cv2.resize (first_gray , (270 , 280))
second = cv2.resize (second_gray , (270 , 280))

first = first.astype (np.float32)
second = second.astype (np.float32)

first_comb = (first * 2 + second * 1) / 3
second_comb = (first + second) / 2
third_comb = (first * 1 + second * 2) / 3

first = first.astype (np.uint8)
first_comb = first_comb.astype (np.uint8)
second_comb = second_comb.astype (np.uint8)
third_comb = third_comb.astype (np.uint8)
second = second.astype (np.uint8)

result = np.concatenate ((first ,first_comb , second_comb , third_comb , second) , axis = 1)
cv2.imwrite ("outputs\output_1_face_morphing.jpg" , result)