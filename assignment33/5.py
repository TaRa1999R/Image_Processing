
import cv2
import numpy as np

def check_white (row , col) :
    ...


def mine_findContours (img) :
    m_contours = []
    for row in range (img.shape[0]) :
        for col in range (img.shape[1]) :
            if img[row , col] == 255 :

                    
#  contours = []
##  visited = np.zeros_like(thresh)
#  for i in range(thresh.shape[0]):
   # for j in range(thresh.shape[1]):
       # if thresh[i,j] == 255 and visited[i,j] == 0:
           # contour = []
           # stack = [(i,j)]
           # visited[i,j] = 1
           # while len(stack) > 0:
               # x,y = stack.pop()
               # contour.append((x,y))
               # for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(-1,1),(1,1)]:
                   # nx,ny = x+dx,y+dy
                   # if nx >= 0 and nx < thresh.shape[0] and ny >= 0 and ny < thresh.shape[1]:
                       # if thresh[nx,ny] == 255 and visited[nx,ny] == 0:
                           # stack.append((nx,ny))
                           # visited[nx,ny] = 1
           # contours.append(np.array(contour))
#  return contours

image = cv2.imread ("inputs\input_1_BW_1.jpg" , cv2.IMREAD_GRAYSCALE)
_ , thresh = cv2.threshold (image , 170 , 255 , cv2.THRESH_BINARY)


# open cv code
# contours , _ = cv2.findContours (thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
# print (contours[5])
# x, y, w, h = cv2.boundingRect (contours[5])
# cv2.rectangle (image , (x,y) , (x+w,y+h) , (0,0,0) , 3)
# cv2.imshow ("" , image)
# cv2.waitKey ()


#my code
contours = mine_findContours (thresh)