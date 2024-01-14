
import cv2
import numpy

img_black = numpy.zeros ((320 , 320))
turn = 1

for repeat in range (8) :
    for row in range (repeat * 40 , ((repeat + 1) * 40)) :
        if turn == 1 :
            multi = [0 , 2 , 4 , 6]

        elif turn == 2 :
            multi = [1 , 3 , 5 , 7]

        for i in multi :
            for col in range (i * 40 , (i + 1) * 40) :
                img_black[row][col] = 255
    
    if turn == 1 :
        turn = 2

    elif turn == 2 :
        turn = 1

cv2.imshow ("result 1", img_black)
cv2.waitKey ()
cv2.imwrite ("assignment26\outputs\output_1_chess_board.jpg" , img_black)