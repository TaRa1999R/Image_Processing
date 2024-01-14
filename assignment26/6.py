
import cv2

image_in = cv2.imread ("assignment26\inputs\input_6.jpg")
black_image = cv2.cvtColor (image_in , cv2.COLOR_BGR2GRAY)
begin = 150
end = 250
for row in range (150) :
    for colomn in range (begin , end) :
        black_image[row][colomn] = 0
    begin -= 1
    end -= 1

triangle = 100
for row in range (150 , 250) :
    for colomn in range (0 , triangle ) :
        black_image[row][colomn] = 0
    triangle -= 1

cv2.imshow ("result 6" , black_image)
cv2.waitKey ()
cv2.imwrite ("assignment26\outputs\output_6.jpg" , black_image)