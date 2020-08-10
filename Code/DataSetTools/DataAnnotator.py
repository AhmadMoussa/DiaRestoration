"""
<Slide Photo Digitalization Software>
    Copyright (C) 2020  Ahmad Yunis Moussa

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import cv2
import numpy as np
import os

ref_point = []
counter = 0

def get_coords(image):

    # clone image to ba able to reset image
    clone = image.copy()

    def shape_selection(event, x, y, flags, params):
        # grab references to the global variables
        global counter, ref_point, crop
        print(counter)
        print(ref_point)
        # if the left mouse button was clicked, record the starting
        # (x, y) coordinates and indicate that cropping is being performed
        if event == cv2.EVENT_LBUTTONDOWN:
            if counter == 0:
                ref_point = [[x, y]]
                counter += 1
            else:
                ref_point.append([x,y])
                counter += 1


        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP and counter==4:
            # record the ending (x, y) coordinates and indicate that
            # the cropping operation is finished
            #ref_point.append((x, y))


            # draw a rectangle around the region of interest
            cv2.polylines(image, np.array([ref_point]), 2, (0, 255, 0))
            cv2.imshow("image", image)

            counter = 0

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", shape_selection)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        # press 'r' to reset the window
        if key == ord("r"):
            image = clone.copy()

        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break

    return ref_point
    # close all open windows
    cv2.destroyAllWindows()

path = "../test_images/"
files = os.listdir(path)
for file in files:
    img = cv2.imread(path + file)
    img = cv2.resize(img, (378, 504))


    clone = img.copy()
    target_coords = get_coords(img)
    print(target_coords)
    flatten = lambda l: [item for sublist in l for item in sublist]
    target_coords = flatten(target_coords)
    print(target_coords)
    target_coords = ' '.join(str(e) for e in target_coords)
    print(target_coords)
    cv2.imwrite(target_coords + " .png", clone)
