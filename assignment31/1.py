
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread ("inputs\input_1_friends.jpg" , cv2.IMREAD_GRAYSCALE)
rows , cols = img.shape

histogram = []
index = []
for n in range (256) :
    index.append (n)
    histogram.append (0)

for i in range (rows) :
    for j in range (cols) :
        histogram [img[i][j]] += 1

# plt.plot (histogram)
# plt.savefig ("outputs\output_1_plot.jpg")

# plt.hist (histogram)
# plt.savefig ("outputs\output_1_hist.jpg")

plt.bar (index , histogram)
plt.savefig ("outputs\output_1_bar.jpg")