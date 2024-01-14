
import math
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from mtcnn.mtcnn import MTCNN


def draw_facebox_and_keypoint (filename , result_list) :
    
    data = plt.imread (filename)
    plt.imshow (data)
    ax = plt.gca ()

    for result in result_list :
        x , y , w , h = result ['box']
        rec = plt.Rectangle ((x,y) , w , h , fill = False , color = 'green')
        ax.add_patch (rec)
        
        for key , value in result['keypoints'].items() :
            dot = plt.Circle (value , radius = 2 , color = 'blue')
            ax.add_patch (dot)
    
    plt.show ()


def EuclideanDistance (source_representation , test_representation) :
    
    euclidean_distance = source_representation - test_representation
    euclidean_distance = np.sum (np.multiply (euclidean_distance , euclidean_distance))
    euclidean_distance = np.sqrt (euclidean_distance)
    return euclidean_distance

def alignment_procedure (img , left_eye , right_eye) :

    x_left , y_left = left_eye
    x_right , y_right = right_eye

    if y_left > y_right :
        poit_3rd = (x_right , y_left)
        direction = -1

    else :
        poit_3rd = (x_left , y_right)
        direction = 1
    
    a = EuclideanDistance (np.array (left_eye) , np.array (poit_3rd))
    b = EuclideanDistance (np.array (right_eye) , np.array (poit_3rd))
    c = EuclideanDistance (np.array (right_eye) , np.array (left_eye))

    if b != 0 and c != 0 :
        cos_a = (b * b + c * c - a * a) / (2 * b * c)
        radian_angle = np.arccos (cos_a)
        degree_angle = (radian_angle * 180) / math.pi

        if direction == -1 :
            degree_angle = 90 - degree_angle

            img = Image.fromarray (img)
            img = np.array (img.rotate (direction * degree_angle))
    
    return img


joey_img = plt.imread ("inputs\input_3_joey.jpeg")
face_detector = MTCNN ()

results = face_detector.detect_faces (joey_img)
draw_facebox_and_keypoint ("inputs\input_3_joey.jpeg" , results)

detection = results [0]
keypoints = detection ["keypoints"]
left_eye = keypoints ["left_eye"]
right_eye = keypoints["right_eye"]

joey_img = alignment_procedure (joey_img , left_eye , right_eye)

plt.imshow (joey_img)
plt.show ()
plt.imsave ("outputs\output_3_align_face.jpg" , joey_img)