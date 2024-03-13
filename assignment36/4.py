
import cv2
import numpy as np 
import argparse


ap = argparse.ArgumentParser ()
ap.add_argument ("--v" , "--video" , help = "outputs\output_4_skin_detector.mp4")
args = vars (ap.parse_args ())

lower_range = np.array ([0 , 48 , 80] , dtype = np.uint8)
upper_range = np.array ([20 , 255 , 255] , dtype = np .uint8)

if not args.get ("video" , False) :
    cap = cv2.VideoCapture (0)

else :
    cap = cv2.VideoCapture (args["video"])

while True :
    grabbed , frm = cap.read ()

    if args.get ("video") and not grabbed :
        break

    frm_hsv = cv2.cvtColor (frm , cv2.COLOR_BGR2HSV)
    skin_mask = cv2.inRange (frm_hsv , lower_range , upper_range)

    kernel = cv2.getStructuringElement (cv2.MORPH_ELLIPSE , (11 , 11))
    skin_mask = cv2.erode (skin_mask , kernel , iterations = 2)
    skin_mask = cv2.dilate (skin_mask , kernel , iterations = 2)

    skin_mask = cv2.GaussianBlur (skin_mask , (3 , 3) , 0)
    skin = cv2.bitwise_and (frm , frm , mask = skin_mask)

    cv2.imshow ("result 4" , np.hstack ([frm , skin]))
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break

cap.release ()