#!/usr/bin/env python
# coding: utf-8

# In[32]:


pip install matplotlib

import cv2
import matplotlib.pyplot as plt


# In[15]:


pip install matplotlib

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\Banner_Pokemon.jpg",cv2.IMREAD_GRAYSCALE)


# In[17]:


cv2.imshow("image",img)
cv2.waitKey(5000)


# In[24]:


cv2.destroyAllWindows()


# In[ ]:


cv2.destroyAllWindow()


# In[26]:


cv2.imwrite(r"C:\Users\Nishanth\Documents\Pictures\Output\Banner_Pokemon_1.jpg", img)
cv2.waitKey(5000)


# In[28]:


plt.imshow(img)


# In[ ]:




