#!/usr/bin/env python
# coding: utf-8

# In[19]:


import cv2
import matplotlib.pyplot as plt


# In[3]:


img = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\Banner_Pokemon.jpg",cv2.IMREAD_GRAYSCALE)


# In[7]:


cv2.imshow("image",img)
cv2.waitKey(50000)


# In[9]:


cv2.destroyAllWindows()


# In[13]:


cv2.imwrite(r"C:\Users\Nishanth\Documents\Pictures\output\Banner_Pokemon.jpg",img)


# In[21]:


plt.imshow(img)


# In[ ]:




