import cv2
import numpy as np

img = cv2.imread('result_0.png')

def improve_contrast_image_using_clahe(cL, tGS, bgr_image: np.array) -> np.array:
    hsv = cv2.cvtColor(bgr_image, cv2.COLOR_RGB2HSV)
    hsv_planes = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=cL, tileGridSize=(tGS, tGS))
    hsv_planes[2] = clahe.apply(hsv_planes[2])
    hsv = cv2.merge(hsv_planes)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)




processed = improve_contrast_image_using_clahe(2, 8, img)
psnr = cv2.PSNR(img, processed)

cv2.imwrite("results/clahe_img_{}_{}_{}.jpg".format(2, 8, psnr), processed)





