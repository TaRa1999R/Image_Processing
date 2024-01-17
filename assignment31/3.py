
import cv2
import numpy as np 

img_lion = cv2.imread ("inputs\input_3_lion.png" , cv2.IMREAD_GRAYSCALE)
# img_spider = cv2.imread ("inputs\input_3_spider.webp", cv2.IMREAD_GRAYSCALE)

l_rows , l_cols = img_lion.shape
# s_rows , s_cols = img_spider.shape

result_lion = np.zeros ((l_rows , l_cols) , dtype = np.uint8)
# result_spider = np.zeros ((s_rows , s_cols) , dtype = np.uint8)

filter_1 = np.array ([[-1 , -1 , -1] ,
                      [-1 , 8 , -1] ,
                      [-1 , -1 , -1]] , dtype = np.uint8)

# filter_2 = np.array ([[-1 , -2 , -1] ,
                    #   [-2 , 4 , -2] ,
                    #   [-1 , -2 , -1]] , dtype = np.uint8)

for i_l in range (1 , l_rows - 1) :
    for j_l in range (1 , l_cols - 1) :
        small_lion = img_lion [i_l - 1 : i_l + 2 , j_l - 1 : j_l + 2]
        result_lion [i_l , j_l] = np.sum (filter_1 * small_lion)

# for i_s in range (1 , s_rows - 1) :
    # for j_s in range (1 , s_cols - 1) :
        # small_spider = img_spider [i_s - 1 : i_s + 2 , j_s - 1 : j_s + 2]
        # result_spider [i_s , j_s] = np.abs (np.sum (filter_2 * small_spider))

cv2.imwrite ("outputs\output_3_lion.jpg" , result_lion)
# cv2.imwrite ("outputs\output_3_spider.jpg" , result_spider)

