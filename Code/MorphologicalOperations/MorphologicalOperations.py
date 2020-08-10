import cv2
import numpy as np


image = cv2.imread('diapic2.jpeg')
print(image.shape)
#image = cv2.resize(image, (600, 800))

cv2.imshow('image', cv2.resize(image, (300, 400)))
cv2.imwrite('imgsforpaper/1orig.png', cv2.resize(image, (1200, 1600)))
cv2.waitKey()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', cv2.resize(gray, (300, 400)))
cv2.imwrite('imgsforpaper/2gray.png', cv2.resize(gray, (1200, 1600)))
cv2.waitKey()


blur = cv2.medianBlur(gray, 5)
cv2.imshow('image', cv2.resize(blur, (300, 400)))
cv2.imwrite('imgsforpaper/3medianBlur.png', cv2.resize(blur, (1200, 1600)))
cv2.waitKey()

sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

cv2.imshow('image', cv2.resize(sharpen, (300, 400)))
cv2.imwrite('imgsforpaper/4sharpen.png', cv2.resize(sharpen, (1200, 1600)))
cv2.waitKey()

thresh = cv2.threshold(sharpen,60,255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('image', cv2.resize(thresh, (300, 400)))
cv2.imwrite('imgsforpaper/5thresh.png', cv2.resize(thresh, (1200, 1600)))
cv2.waitKey()


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=7)
cv2.imshow('image', cv2.resize(open, (300, 400)))
cv2.waitKey()



cnts = cv2.findContours(open, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
print(len(cnts))


min_area = 0
max_area = 5000000
image_number = 0
for c in cnts:
    area = cv2.contourArea(c)
    if area > min_area and area < max_area:
        x,y,w,h = cv2.boundingRect(c)
        ROI = image[y:y+h, x:x+h]
        #cv2.imwrite('ROI_{}.png'.format(image_number), ROI)
        cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
        image_number += 1


cv2.imshow('sharpen', cv2.resize(sharpen, (300, 400)))
cv2.imwrite('sharpen.png', sharpen)
cv2.imshow('open', cv2.resize(open, (300, 400)))

cv2.imwrite('open.png', open)
cv2.imshow('thresh', cv2.resize(thresh, (300, 400)))
cv2.imwrite('thresh.png', thresh)
cv2.imshow('image', cv2.resize(image, (300, 400)))
cv2.imwrite('imgsforpaper/6image.png', cv2.resize(image, (1200, 1600)))
cv2.imwrite('image.png', image)
cv2.waitKey()