
import cv2
import numpy as np

def filter_3 (img , adress) :
    rows , cols = img.shape
    result = np.ones ((rows , cols) , dtype = np.uint8)

    filter = np.ones ((3 , 3)) / 9

    for i in range (1 , rows - 1) :
        for j in range (1 , cols - 1) :
            small = img [i -1 : i + 2 , j - 1 : j + 2]
            result [i , j] = np.sum (filter * small)
        
    cv2.imwrite (adress , result)



def filter_5 (img , adress) :
    rows , cols = img.shape
    result = np.ones ((rows , cols) , dtype = np.uint8)

    filter = np.ones ((5 , 5)) / 25

    for i in range (2 , rows -2) :
        for j in range (2 , cols - 2) :
            small = img [i - 2 : i + 3 , j - 2 : j + 3]
            result = np.sum (filter * small)

    cv2.imwrite (adress , result)


def filter_15 (img , adress) :
    rows , cols = img.shape
    result = np.ones ((rows , cols) , dtype = np.uint8)

    filter = np.ones ((15 , 15)) / 255

    for i in range (7 , rows - 7) :
        for j in range (7 , cols - 7) :
            small = img [i - 7 : i + 8 , j - 7 : j + 8]
            result = np.sum (filter * small)

    cv2.imwrite (adress , result)


img_xray = cv2.imread ("inputs\input_5_xray_noisy.png" , cv2.IMREAD_GRAYSCALE)
img_board = cv2.imread ("inputs\input_5_board_noisy.png" , cv2.IMREAD_GRAYSCALE)
img_noisy = cv2.imread ("inputs\input_5_image_noisy.png" , cv2.IMREAD_GRAYSCALE)

filter_3 (img_xray , "outputs\output_5_xray_3.jpg")
filter_5 (img_xray , "outputs\output_5_xray_5.jpg")
filter_15 (img_xray , "outputs\output_5_xray_15.jpg")

filter_3 (img_board , "outputs\output_5_board_3.jpg")
filter_5 (img_board , "outputs\output_5_board_5.jpg")
filter_15 (img_board , "outputs\output_5_board_15.jpg")

filter_3 (img_noisy , "outputs\output_5_circle_3.jpg")
filter_5 (img_noisy , "outputs\output_5_circle_5.jpg")
filter_15 (img_noisy , "outputs\output_5_circle_15.jpg")