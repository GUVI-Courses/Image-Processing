#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2
import numpy as np

# read image
img = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\pic1.jpg")

# get dimensions of image
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Dimension    : ', dimensions)
print('Image Height       : ', height)
print('Image Width        : ', width)
print('Number of Channels : ', channels)
print('Image Shape        :',  img.shape)

# Resizing
imgResize = cv2.resize(img,(300,200)) # width comes first

# Cropping
imgCropped = img[0:200, 200:500]  # height comes first

# Blurring
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(11,11),0)# object, kernel size (odd no), sigmax

cv2.imshow("Image", img)
#cv2.imshow("Resized Image", imgResize)
#cv2.imshow("Cropped Image", imgCropped)
cv2.imshow("Blurring",imgBlur)
cv2.waitKey(0)


# In[ ]:




