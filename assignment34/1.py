
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_1_joey.jpeg")

# cv2 code
gray = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)
print ("gray:" , gray[0][30:45])

# my code
b , g , r = cv2.split (img)
print ("blue:" , b[0][30:45])
print ("green:" , g[0][30:45])
print ("red:" , r[0][30:45])

my_gray = np.zeros (img.shape , dtype = np.uint8)

# for i in range (img.shape [0]) :
    # for j in range (img.shape [1]) :
        # my_gray [i , j] = (b [i , j] + g [i , j] + r [i , j]) // 3

result = np.hstack ((gray , b , g , r ))
cv2.imshow ("result 1" , result)
cv2.waitKey ()
# cv2.imwrite ("outputs\output_1friends_gray.jpg" , img)