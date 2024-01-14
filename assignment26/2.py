
import cv2
import numpy

input_list = ["assignment26\inputs\input_2_girl.jpg" , "assignment26\inputs\input_2_boy.jpg"]
output_list = ["assignment26\outputs\output_2_girl.jpg" , "assignment26\outputs\output_2_boy.jpg"]

for i in range (2) :
    img = cv2.imread(input_list[i])
    if i == 0 :
        row_range = 645
        col_range = 645

    elif i == 1 :
        row_range = 1202
        col_range = 900
    
    for row in range (row_range) :
        for col in range (col_range) :
            img[row][col] = 255 - img[row][col]

    cv2.imshow ("result 2" , img)
    cv2.waitKey()
    cv2.imwrite (output_list[i] , img)