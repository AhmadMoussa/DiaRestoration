import numpy as np
import cv2

imgs = np.load('imgs_test_np.npz')['arr_0']

cv2.imshow("img",imgs[5])
cv2.waitKey()