
import cv2
import numpy as np 

img = cv2.imread ("inputs\input_1_joey.jpeg")

# cv2 code
gray = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)

# my code
b , g , r = cv2.split (img)
result = np.zeros ((img.shape [0] , img.shape [1]) , dtype = np.uint8)
for i in range (img.shape[0]) :
    for j in range (img.shape[1]) :
        result[i ,j] = (0.2989 * r[i , j]) + (0.5870 * g[i , j]) + (0.1140 * b[i , j])

cv2.imshow ("result 1" , gray)
cv2.waitKey ()
cv2.imshow ("result 1" , result)
cv2.waitKey ()
cv2.imwrite ("outputs\output_1friends_gray.jpg" , result)