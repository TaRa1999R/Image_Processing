
import cv2

full_text = cv2.imread ("inputs\input_4_full.png")
code_breaker = cv2.imread ("inputs\input_4_check.png")

for row in range (full_text.shape[1]) :
    for col in range (full_text.shape[0]) :
        full_text[row][col] = 255 - full_text[row][col]

for row in range (code_breaker.shape[1]) :
    for col in range (code_breaker.shape[0]) :
        code_breaker[row][col] = 255 - code_breaker[row][col]

secret_text = cv2.subtract (full_text , code_breaker)

for row in range (secret_text.shape[1]) :
    for col in range (secret_text.shape[0]) :
        secret_text[row][col] = 255 - secret_text[row][col] 

cv2.imwrite ("outputs\output_4_secret_text.png" , secret_text)