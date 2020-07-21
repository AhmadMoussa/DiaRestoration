# Dia Restoration

Have some old Slide Photos laying around (Dia photos in german)? Or some old family photos that are pretty faded and torn? You also have no clue when these images were taken? Well, look no further! This repo gotchu!

## Objectives

1. Improve quality of dia/old image photo
2. Estimation of data an image was taken
3. Estimation of the age of persons in the image

## Introduction and Background

Slide photos were a popular cost effective way to record images in the 50 and 60s. But this type of photo has quickly fallen out of popularity with the rise of the digital image and the smart-phone. This relatively quick transition and shift in technology left many families with stacks of old slide photos and no good way of digitalizing them.
This paper attempts the restoration and digitalization of these images as well as the improvement of the quality of these images, without having to invest in a dedicated hardware device for this purpose.

Hardware devices have been devised for the purpose of digitalization of old dia images. But generally these devices can be quiet expensive and are generally used once for the digitalization of some images, and later lacks any purpose whatsoever. Alternatively services exist to which you can send in your slides via mail and digitalize them for a one time fee. For many people such a device and/or service might not be worth the price, as they have only a handfull of slide films at home.

Additionally we find it important to estimate the date of taking the photo as it gives important information to the owner.

## Pipeline

There's a number of steps we have to follow to achieve good quality results:

1. First the diorama photo should be captured while it is well backlit.
2. We need to locate and crop out the important area of the diorama (the small image).
3. Correct the orientation of the image.
3. Correct colors of image (dias are generally faded and have yellow-ish colors)
4. Improve resolution of image

## Part 1 - ROI Detection:

The first problem we need to consider is locating the important part of the slide image within an image. We have attempted to locate the ROI with morphological computer vision techniques, but only with mild success.

We found that the best way to detect the bounding box of the ROI was using a convolutional neural network that we trained on manually annotated counding box corner coordinates. The dataset consisted of around 1000 images, and we performed data augmentation by randomly shifting/translating the image up/down/left/right along with the bounding box coordinates by a random amount (such that the ROI is still in the image). We get a detection accuracy of {insert accuracy here}. It works well if the image is aligned with borders of the camera.

## Part 2 - Perspective Transform:

The detected ROI might not always be perfectly perpendicular with respect to the capturing camera. A perspective Transform can help alleviate a skewed or slanted image.

## Part 3 - Image enhancement:

### 3.1 - CLAHE (Contrast Limited Adaptive Histogram Equalization):

Learn more about it [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html)

Other techniques [here](https://stackoverflow.com/questions/56905592/automatic-contrast-and-brightness-adjustment-of-a-color-photo-of-a-sheet-of-pape) 

### 3.2 - De-blurring:

Images can be be-blurred with a simple sharpening filter, but this generally does not give good results as it tends to accentuate defects in the image. Deep learning methods have also been devised for this purpose.

Deep Learning de-blurring candidates: [DeblurGAN-v2: Deblurring (Orders-of-Magnitude) Faster and Better](https://github.com/TAMU-VITA/DeblurGANv2)

### 3.3 - Upscaling and/or SR (Super Resolution):

This step is largely optional and depends on the type of camera you used to capture the DIA image. In my case the resolution of the captured images was already significantly high.

Some candidate methods for performing this super-resolution [LFFN (Lightweight Feature Fusion Network for Single Image Super-Resolution)](https://github.com/qibao77/LFFN)

## Part 4 - Image Age Estimation:

I felt that this was an additional feature that could be important for these types of images. A lot of these images are unlabelled and could be taken in any time period. Estimating the year when an image was taken can provide additional important context.
