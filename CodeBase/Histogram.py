#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
# import Numpy
import numpy as np
# reading an image using imreadmethod
my_img = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\Banner_Pokemon.jpg", 0)
equ = cv2.equalizeHist(my_img)
# stacking both the images side-by-side orientation
res = np.hstack((my_img, equ))
# showing image input vs output
cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




