#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\pic2.jpg")

# Step 1: Define 4 corner points , use any photo editor like paint to get pixel location of the points
pts1 = np.float32([[85,30],[150,30],[86,125],[150,125]])

# Step 2: Define location of the points
width, height = 250, 350 # getting required size by taking care of height & width ratio of card
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Step 3: Make matrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)

# Get Output image based on the above matrix
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image",img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)


# In[ ]:


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success,frame = cap.read()

# Step 1: Define 4 corner points , use any photo editor like paint to get pixel location of the points
pts1 = np.float32([[85,30],[150,30],[86,125],[150,125]])

# Step 2: Define location of the points
width, height = 250, 350 # getting required size by taking care of height & width ratio of card
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Step 3: Make matrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)

# Get Output image based on the above matrix
vidOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image",img)
cv2.imshow("Output", vidOutput)
cv2.waitKey(0)

