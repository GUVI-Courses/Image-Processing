#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\pic1.jpg")

# creating a matrix of ones of size 5,5 with object unsigned int
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,150,200) # object, Threshold1, threshold 2
cv2.imshow("Canny Image",imgGray)

cv2.waitKey(0)


# In[ ]:




