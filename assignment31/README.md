# Assignment 31 : Convolution and Histogram

## How to Install
Run following command :
```
pip install -r requirments.txt
```

## First part : Histogram
In this assignment we calculate the following picture's histogram, and visualized it :
![Alt text](inputs/input_1_friends.jpg)

firs we used a plot diagram ==> plt.plot()

![Alt text](outputs/output_1_plot.jpg)

then we used a histogram diagram ==> plt.hist()

![Alt text](outputs/output_1_hist.jpg)

and finally we used a bar chart ==> plt.bar()

![Alt text](outputs/output_1_bar.jpg)

## Second part : Foreground Focus, Blur Background
In this assignment we hblurresd the background and draw the focus on the white flower on the foreground.

the input picture :
![Alt text](inputs/input_2_rose.jpg)

the output photo :
![Alt text](outputs/output_2_rose.jpg)

## Thirs part : Edge Detection
In this assignment we use two different edge detection method to find the following pictures edge :
![Alt text](inputs/input_3_lion.png)
![Alt text](inputs/input_3_spider.webp)

for the lion picture we used 'Sobel Operator', and the output is :
![Alt text](outputs/output_3_lion.jpg)

for the spider picture we used 'Laplacian Operator', and the result is:

![Alt text](outputs/output_3_spider.jpg)

## Fourth part : Vertical and Horizental Edge Detecion
In this assignment we use two different filter on a same picture, which you can see below :
![Alt text](inputs/input_4_bilding.png)

one of the filters is a horizental edge detection. It bolds horizental edges in the picture and it will give us the following output:
![Alt text](outputs/output_4_horizental.jpg)

the other filter is a vertical edge dection. It bolds vertical edges in the picture and it will give us the following output:
![Alt text](outputs/output_4_vertical.jpg)

## Fifth part : Noise Reduction
In this assignment we use three noise reduction in diffrent scales on three diffrent photo :

first photo is a X-RAY photo :
![Alt text](inputs/input_5_xray_noisy.png)

second photo is an electronic board :

![Alt text](inputs/input_5_board_noisy.png)

and third photo is a noisy picture of geometric shapes :

![Alt text](inputs/input_5_image_noisy.png)

Each photo is filtered in three different scale : 3 * 3, 5 * 5, and 15 * 15.

first photo's result => 

3 * 3 :
![Alt text](outputs/output_5_xray_3.jpg)

5 * 5 :
![Alt text](outputs/output_5_xray_5.jpg)

15 * 15 :
![Alt text](outputs/output_5_xray_15.jpg)

second photo's result => 

3 * 3 :

![Alt text](outputs/output_5_board_3.jpg)

5 * 5 :

![Alt text](outputs/output_5_board_5.jpg)

15 * 15 :

![Alt text](outputs/output_5_board_15.jpg)

second photo's result => 

3 * 3 :

![Alt text](outputs/output_5_circle_3.jpg)

5 * 5 :

![Alt text](outputs/output_5_circle_5.jpg)

15 * 15 :

![Alt text](outputs/output_5_circle_15.jpg)