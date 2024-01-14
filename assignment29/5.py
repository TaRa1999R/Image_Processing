
import random
import cv2
import numpy as np

cap = cv2.VideoCapture ("inputs\input_5_cars.mp4")
fps = cap.get (cv2.CAP_PROP_FPS)

ids = []
while len (ids) < 350 :
    random_id = random.randint (0 , 15*fps)
    if random_id not in ids :
        ids.append (random_id)

frames = []
for id in ids :
    cap.set (cv2.CAP_PROP_POS_FRAMES , id)
    _, frame = cap.read ()
    frame = frame.astype (np.float32)
    frames.append (frame)
cap.release ()
frame_sum = np.zeros (frame.shape)

for frm in frames :
    frame_sum += frm

final_frame = frame_sum / len (frames)
final_frame = final_frame.astype (np.uint8)
cv2.imwrite ("outputs\output_5_background_estimation.jpg" , final_frame)