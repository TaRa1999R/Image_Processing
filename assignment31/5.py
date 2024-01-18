
import cv2
import numpy as np

def filtering (img , adress , n) :
    rows , cols = img.shape
    result = np.ones ((rows , cols) , dtype = np.uint8)

    filter = np.ones ((n , n)) / (n * n)
    k = (n - 1) // 2

    for i in range (k , rows - k) :
        for j in range (k , cols - k) :
            small = img [i - k : i + k + 1 , j - k : j + k + 1]
            result [i , j] = np.sum (filter * small)
        
    cv2.imwrite (adress , result)



# def filter_5 (img , adress) :
    # rows , cols = img.shape
    # result = np.ones ((rows , cols) , dtype = np.uint8)
# 
    # filter = np.ones ((5 , 5)) / 25
# 
    # for i in range (2 , rows -2) :
        # for j in range (2 , cols - 2) :
            # small = img [i - 2 : i + 3 , j - 2 : j + 3]
            # result = np.sum (filter * small)
# 
    # cv2.imwrite (adress , result)
# 
# 
# def filter_15 (img , adress) :
    # rows , cols = img.shape
    # result = np.ones ((rows , cols) , dtype = np.uint8)
# 
    # filter = np.ones ((15 , 15)) / 255
# 
    # for i in range (7 , rows - 7) :
        # for j in range (7 , cols - 7) :
            # small = img [i - 7 : i + 8 , j - 7 : j + 8]
            # result = np.sum (filter * small)
# 
    # cv2.imwrite (adress , result)


img_xray = cv2.imread ("inputs\input_5_xray_noisy.png" , cv2.IMREAD_GRAYSCALE)
img_board = cv2.imread ("inputs\input_5_board_noisy.png" , cv2.IMREAD_GRAYSCALE)
img_noisy = cv2.imread ("inputs\input_5_image_noisy.png" , cv2.IMREAD_GRAYSCALE)

filtering (img_xray , "outputs\output_5_xray_3.jpg" , 3)
filtering (img_xray , "outputs\output_5_xray_5.jpg" , 5)
filtering (img_xray , "outputs\output_5_xray_15.jpg" , 15)
 
filtering (img_board , "outputs\output_5_board_3.jpg" , 3)
filtering (img_board , "outputs\output_5_board_5.jpg" , 5)
filtering (img_board , "outputs\output_5_board_15.jpg" , 15)
 
filtering (img_noisy , "outputs\output_5_circle_3.jpg" , 3)
filtering (img_noisy , "outputs\output_5_circle_5.jpg" , 5)
filtering (img_noisy , "outputs\output_5_circle_15.jpg" , 15)