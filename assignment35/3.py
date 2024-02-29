
import cv2
import numpy as np 
import mediapipe as mp

mp_pose = mp.solutions.pose 
pose = mp_pose.Pose (static_image_mode = False , model_complexity = 1 , smooth_landmarks = True , min_detection_confidence = 0.5 , min_tracking_confidence = 0.5)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture (0)
writer = cv2.VideoWriter ("outputs\output_3_body_landmark.mp4" , cv2.VideoWriter_fourcc(*'mpv4') , 10 , (640 , 480))


while True :
    _ , frm = cap.read ()

    frm.flags.writeable = False
    frm = cv2.cvtColor (frm , cv2.COLOR_BGR2RGB)
    result = pose.process (frm)
    
    frm.flags.writeable = True
    frm = cv2.cvtColor (frm , cv2.COLOR_RGB2BGR)

    if result.pose_landmarks :
        mp_drawing.draw_landmarks (frm , 
                                   result.pose_landmarks , 
                                   mp_pose.POSE_CONNECTIONS , 
                                   landmark_drawing_spec = mp_drawing.DrawingSpec (color = (170 , 0 , 140) , thickness = 2 , circle_radius = 2) , 
                                   connection_drawing_spec = mp_drawing.DrawingSpec (color = (170 , 140 , 0) , thickness = 2 , circle_radius = 2))
    

    cv2.imshow ("result 3" , frm )
    writer.write (frm)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break

writer.release ()