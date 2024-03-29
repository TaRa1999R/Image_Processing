# Assignment 34 : Supplementary Topics

## How to Install
Run following command :
```
pip install -r requirments.txt
```

## First part : Portable Network Graphics
In this assignment my code transparent a Microsoft logo and remove it's background.

![alt text](outputs/output_1_logo.png)

## Second part : Color Recognition
In this assignment my code detect different colors, such as : 🔴🟠🟡🟢🔵🟣⚫⚪

⚫ Black color :
![alt text](outputs/output_2_detect_black.png)
⚪ White color :
![alt text](outputs/output_2_detect_white.png)
🔴 Red color :
![alt text](outputs/output_2_detect_red.png)
🟠 Orange color :
![alt text](outputs/output_2_detect_orange.png)
🟡 Yellow color :
![alt text](outputs/output_2_detect_yellow.png)
🟢 Green color :
![alt text](outputs/output_2_detect_green.png)
🔵 Blue color :
![alt text](outputs/output_2_detect_blue.png)
🟣 Purple color :
![alt text](outputs/output_2_detect_purple.png)

## Third part : MediaPipe
In this assignment I used mediapipe to detect body landmarks on webcam stream , you can see the result in a video in outputs folder.
Here is a frame of this video :

![alt text](outputs/output_3_body_landmark.png)

## Fourth part : PIL (Python Image Library )
In this assignment I used PILLOW (PIL) library to do diffrent analysis on a photo :

1. Read a color image

![alt text](inputs/input_4_friends.jpg)

2. Write a persian text on image

![alt text](outputs/output_4_persian_text.jpg)

3. Calculate 3 histogram and show with plt

![alt text](outputs/output_4_histogram.jpg)

4. Equalize the imge histogram

![alt text](outputs/output_4_equalized.jpg)

5. Convert imge to grayscale

![alt text](outputs/output_4_gray_img.jpg)

6. Calculate grayscale imge's histogram

![alt text](outputs/output_4_gray_histogram.jpg)

7. Equalize the grascale histogram

![alt text](outputs/output_4_gray_equalized.jpg)

## Fifth part : Image Encryption and Decryption
In this assignment I used a photo as an input, and each time I run the code a new key will be made, and by that I make an encryption model of my
photo and decrypted it to the main photo.

Input photo :
![alt text](inputs/input_5_Mona_Lisa.jpg)
Encrypted form :
![alt text](outputs/output_5_encrypted_image.jpg)
Decrypted form :
![alt text](outputs/output_5_dencrypted_image.jpg)