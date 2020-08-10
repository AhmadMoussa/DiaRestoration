import keras
import os
import numpy as np
import cv2
from keras.models import Model
from keras.layers import Input, Conv2D, Dense, Flatten

net_in = Input(shape=(504,378,3))
conv1 = Conv2D(16,7, activation="relu")(net_in)
conv12 = Conv2D(16,7, strides=(2,2), activation="relu")(conv1)


conv2 = Conv2D(48,3, activation="relu")(conv12)
conv22 = Conv2D(48,3, strides=(2,2), activation="relu")(conv2)


conv3 = Conv2D(64,3, activation="relu")(conv22)
conv32 = Conv2D(64,3, strides=(2,2), activation="relu")(conv3)


conv4 = Conv2D(96,3, strides = (2,2), activation="relu")(conv32)
conv42 = Conv2D(128,3, strides=(2,2), activation="relu")(conv4)

flat = Flatten()(conv42)
dense = Dense(8)(flat)

model = Model(net_in, dense)
model.summary()

model.load_weights("../model_weights/model_980.h5")

path = "../test_images/"
files = os.listdir(path)
def perspective_transform(img, coords, i):

    print(coords)
    W = int(-(coords[0][0] - coords[1][0]) * 2)
    H = int(-(coords[0][1] - coords[3][1]) * 2)
    print(W)
    print(H)

    # Define points in input image: top-left, top-right, bottom-right, bottom-left
    pts0 = np.float32(coords)

    # Define corresponding points in output image
    pts1 = np.float32([[0, 0], [W, 0], [W, H], [0, H]])

    # Get perspective transform and apply it
    M = cv2.getPerspectiveTransform(pts0, pts1)
    result = cv2.warpPerspective(img, M, (W, H))

    # Save reult
    cv2.imwrite('../folder_for_test_results/ROI_{}.png'.format(i), result)

for num, file in enumerate(files):
    orig = cv2.imread(os.path.join(path, file))
    img = cv2.resize(orig, (378, 504))

    Xratio =  orig.shape[1] / 378
    Yratio =  orig.shape[0] / 504


    prediction = model.predict(np.array([img]) / 255)

    print(file)

    prediction = prediction[0]
    prediction = [prediction[i:i + 2] for i in range(0, len(prediction), 2)]
    prediction[0][0] = int(prediction[0][0] * Xratio)
    prediction[1][0] = int(prediction[1][0] * Xratio)
    prediction[2][0] = int(prediction[2][0] * Xratio)
    prediction[3][0] = int(prediction[3][0] * Xratio)

    prediction[0][1] = int(prediction[0][1] * Yratio)
    prediction[1][1] = int(prediction[1][1] * Yratio)
    prediction[2][1] = int(prediction[2][1] * Yratio)
    prediction[3][1] = int(prediction[3][1] * Yratio)


    #file = [int(coor) for coor in file[:-4].split(" ")[:-1]]
    #file = [file[i:i + 2] for i in range(0, len(file), 2)]
    #print(file)

    print(prediction)

    #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.polylines(orig, np.int32([[prediction]]), 2, (0, 255, 0))
    #cv2.polylines(img, np.int32([[file]]), 2, (0, 0, 255))
    cv2.imwrite("../folder_for_test_results/img_{}.png".format(num), orig)

    perspective_transform(orig, prediction, num)
    #roi_crop(img, prediction)

