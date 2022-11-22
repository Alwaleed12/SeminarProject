from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng
import datetime
import matplotlib.pyplot as plt


rng.seed(12345)

def thresh_callback(val):
    start=datetime.datetime.now()
    threshold = val

    # Detect edges using Canny
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)

    # Find contours
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Draw contours
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)

    # Show in a window
    cv.imshow('Contours', drawing)
    
    # Added Timing
    end=datetime.datetime.now()
    difference= end-start
    seconds = difference.total_seconds()
    miliseconds = seconds * 1000
    print('the results in seconds = ', seconds)
    print('the results in milisencods', miliseconds)
    

# Load source image
parser = argparse.ArgumentParser(description='Code for Finding contours in your image tutorial.')
parser.add_argument('--input', help='Path to input image.', default='cars.png')
args = parser.parse_args()

src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

# counting objects
# gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap='gray')

# blur = cv.GaussianBlur(gray, (11, 11), 0)
# plt.imshow(blur, cmap='gray')

# canny = cv.Canny(blur, 30, 150, 3)
# plt.imshow(canny, cmap='gray')

# dilated = cv.dilate(canny, (1, 1), iterations=0)
# plt.imshow(dilated, cmap='gray')

# (cnt, hierarchy) = cv.findContours(
#     dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# rgb = cv.cvtColor(src, cv.COLOR_BGR2RGB)
# cv.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

# print("coins in the image : ", len(cnt))
 
# plt.imshow(rgb)

# Convert image to gray and blur it
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))


# Create Window
source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)
max_thresh = 255
thresh = 100 # initial threshold
cv.createTrackbar('Canny Thresh:', source_window, thresh, max_thresh, thresh_callback)
thresh_callback(thresh)

cv.waitKey()