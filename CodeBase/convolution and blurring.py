#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Importing the modules 
import cv2 
import numpy as np 

# Reading the image 
image = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\waffle.jpg") 

# Applying the filter 
averageBlur = cv2.blur(image, (5, 5)) 
# Applying the filter 
gaussian = cv2.GaussianBlur(image, (3, 3), 0) 

# Showing the image 
cv2.imshow('Original', image) 
cv2.imshow('Average blur', averageBlur) 
cv2.imshow('Gaussian blur', gaussian)

cv2.waitKey() 
cv2.destroyAllWindows() 


# In[ ]:





# In[ ]:




