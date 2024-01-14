
import os
import cv2
import numpy as np

rt_images = []
rb_images = []
lt_images = []
lb_images = []

rt_path = os.listdir ("inputs\input_2_right_top")
rb_path = os.listdir ("inputs\input_2_right_bottom")
lt_path = os.listdir ("inputs\input_2_left_top")
lb_path = os.listdir ("inputs\input_2_left_bottom")

for path in rt_path : 
    path = f"inputs\input_2_right_top\{path}"
    img_rt = cv2.imread (path)
    img_rt = img_rt.astype (np.float32)
    rt_images.append (img_rt)

for path in rb_path :
    path = f"inputs\input_2_right_bottom\{path}"
    img_rb = cv2.imread (path)
    img_rb = img_rb.astype (np.float32)
    rb_images.append (img_rb)

for path in lt_path :
    path = f"inputs\input_2_left_top\{path}"
    img_lt = cv2.imread (path)
    img_lt = img_lt.astype (np.float32)
    lt_images.append (img_lt)

for path in lb_path :
    path = f"inputs\input_2_left_bottom\{path}"
    img_lb = cv2.imread (path)
    img_lb = img_lb.astype (np.float32)
    lb_images.append (img_lb)

final_rt = np.zeros (img_rt.shape)
final_rb = np.zeros (img_rb.shape)
final_lt = np.zeros (img_lt.shape)
final_lb = np.zeros (img_lb.shape)

for rt in rt_images :
    final_rt += rt

for rb in rb_images :
    final_rb += rb

for lt in lt_images :
    final_lt += lt

for lb in lb_images :
    final_lb += lb

final_rt = final_rt / len (rt_images)
final_rt = final_rt.astype (np.uint8)

final_rb = final_rb / len (rb_images)
final_rb = final_rb.astype (np.uint8)

final_lt = final_lt / len (lt_images)
final_lt = final_lt.astype (np.uint8)

final_lb = final_lb / len (lb_images)
final_rb = final_rb.astype (np.uint8)

final_top = np.concatenate ((final_lt , final_rt) , axis = 1)
final_bottom = np.concatenate ((final_lb , final_rb) , axis = 1)
final_img = np.concatenate ((final_top , final_bottom) , axis = 0)

cv2.imwrite ("outputs\output_2_black_hole.jpg" , final_img)