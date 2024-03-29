# Assignment 34 : Color Image Processing

## How to Install
Run following command :
```
pip install -r requirments.txt
```

## First part : Convert Color Image to GrayScale Image
In this assignment I wrote a code to convert a color image to a grayscale image. The main code is :
```
gray_image = cv2.cvtColor (image , cv2.COLOR_BGR2GRAY)
```
or
```
img = cv2.imread ("address" , cv2.IMREAD_GRAYSCALE)
```
as you can see my code's result are same as the above codes result. Just run my code.

![alt text](outputs/output_1_joey_gray.jpg)

## Second part : Rainbow
In this assignment I drew a rainbow by opencv library.
![alt text](outputs/output_2_rainbow.jpg)

## Thirs part : Conver watermelon to Materwelon
In this assignment I convert a picture of watermelon to a materwelon, which means I changed red color to green and green color to red.
![alt text](outputs/output_3_watermelon.jpg)

## Fourth part : Solving Rubik Cube
In this assignment I used an unsolved rubik cube as an input, and a solved rubik cube will be seen as an output.

input :

![alt text](inputs/input_4_rubik.png)

output with RGB colors:

![alt text](outputs/output_4_rubik_RGB.jpg)

output with CMY color :

![alt text](outputs/output_4_rubik_CMY.jpg)

## Fifth part : Microsoft Logo
In this assignment I designed a microsoft logo.
![alt text](outputs/output_5_microsoft_logo.jpg)