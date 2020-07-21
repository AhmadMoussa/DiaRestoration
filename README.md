# Dia Restoration

Have some old Slide Photos laying around (Dia photos in german)? Or some old family photos that are pretty faded and torn? You also have no clue when these images were taken? Well, look no further! This repo gotchu!

## Objectives

1. Improve quality of dia/old image photo
2. Estimation of data an image was taken
3. Estimation of the age of persons in the image

## Introduction and Background

Slide photos were a popular cost effective way to record images in the 50 and 60s. But this type of photo has quickly fallen out of popularity with the rise of the digital image and the smart-phone. This relatively quick transition and shift in technology left many families with stacks of old slide photos and no good way of digitalizing them.
This paper attempts the restoration and digitalization of these images as well as the improvement of the quality of these images, without having to invest in a dedicated hardware device for this purpose.
Additionally we find it important to estimate the date of taking the photo as it gives important information to the owner.

## Pipeline

There's a number of steps we have to follow to achieve good quality results:

1. First the diorama photo should be captured while it is well backlit.
2. We need to locate and crop out the important area of the diorama (the small image).
3. Correct the orientation of the image.
3. Correct colors of image (dias are generally faded and have yellow-ish colors)
4. Improve resolution of image

## Part 1: ROI Detection

The first problem we need to consider is locating the important part of the slide image within an image. We have attempted to locate the ROI with morphological computer vision techniques, but only with mild success.

We found that the best way to detect the bounding box of the ROI was using a convolutional neural network that we trained on manually annotated counding box corner coordinates. The dataset consisted of around 1000 images, and we performed data augmentation by randomly shifting/translating the image up/down/left/right along with the bounding box coordinates by a random amount (such that the ROI is still in the image). We get a detection accuracy of {insert accuracy here}. It works well if the image is aligned with borders of the camera.

## Part 2: Perspective Transform

The detected ROI might not always be perfectly perpendicular with respect to the capturing camera. A perspective Transform can help alleviate a skewed or slanted image.

## Part 3: Image enhancement

### 3.1: CLAHE (Contrast Limited Adaptive Histogram Equalization)

Learn more about it [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html)

Other techniques [here](https://stackoverflow.com/questions/56905592/automatic-contrast-and-brightness-adjustment-of-a-color-photo-of-a-sheet-of-pape) 
