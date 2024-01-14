
import cv2

room = cv2.imread ("inputs\input_6_room.jpg")
floor = cv2.imread ("inputs\input_6_floor.jpg")
mask = cv2.imread ("inputs\input_6_mask.jpg")

reversed_mask = 255 - mask

mask = mask / 255.0
masked_floor = floor * mask

reversed_mask = reversed_mask / 255.0
masked_room = room * reversed_mask

decorated_room = masked_floor + masked_room

cv2.imwrite ("outputs\output_6_virtual_decorator.jpg" , decorated_room)