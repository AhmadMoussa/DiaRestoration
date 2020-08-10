import os
import numpy as np
import cv2

def load_data(data_path):
    imgs = []
    labels = []
    for file in os.listdir(data_path):
        imgs.append(cv2.imread(os.path.join(data_path, file)))

        label = file[:-4].split(" ")
        label = label[:-1]
        for i, num in enumerate(label):
            label[i] = int(num)

        labels.append(label)
    return np.array(imgs), np.array(labels)

data_path = "test_slant"
imgs, labels = load_data(data_path)
np.savez_compressed("imgs_test_np", imgs)
np.savez_compressed("labels_test_np", labels)