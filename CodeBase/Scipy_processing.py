#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install scipy')


# In[13]:


from scipy import misc

import imageio
import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt
 
# for grascaling the image
img = imageio.imread(r"C:\Users\Nishanth\Documents\Pictures\pic2.jpg")
 
print(img.shape)
print(img.dtype)
 
plt.imshow(img)
plt.show()

img = misc.face(gray = True) 
x, y = img.shape

plt.imshow(flip)
plt.show()
 
# Cropping the image
crop = img[x//3: - x//8, y//3: - y//8]
 
flip = np.flipud(img)
 
plt.imshow(crop)
plt.show()


# In[ ]:





# In[ ]:




