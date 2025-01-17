#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\pic1.jpg")

# creating a matrix of ones of size 5,5 with object unsigned int
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgDilation = cv2.dilate(imgGray, kernel, iterations=1) # check by increased iteration
imgEroded = cv2.erode(imgGray, kernel, iterations=1)

cv2.imshow("Dilation Image",imgDilation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)


# In[ ]:




