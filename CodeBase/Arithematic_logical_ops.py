#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[3]:


image1 = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\Image_1.jpg")
image2=  cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\Image_2.jpg")


# In[7]:


#add function

image3= cv2.add(image1,image2)

#view
#cv2.imshow('add image',image3)
#cv2.waitKey(0)


# In[9]:


weightedsum= cv2.addWeighted(image1,0.6,image2,0.4,0)


# In[11]:


cv2.imshow('add image',image3)
cv2.waitKey(0)


# In[13]:


#subtraction
image4= cv2.subtract(image1,image2)
cv2.imshow('subtract image',image4)
cv2.waitKey(0)


# In[31]:


image1 = cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\binary_pic1.png")
image2=  cv2.imread(r"C:\Users\Nishanth\Documents\Pictures\binary_pic2.png")


# In[39]:


#AND
final_AND = cv2.bitwise_xor(image2,image1,mask=None)

cv2.imshow('XOR',final_AND)
cv2.waitKey(0)


# In[41]:


final_NOT = cv2.bitwise_not(image2,mask=None)

cv2.imshow('XOR',final_NOT)
cv2.waitKey(0)


# In[23]:


import cv2
import numpy as np

#grayscale image
img = np.zeros((512,512))

print(img.shape)

# Adding color functionality and making above pic blue
img2 = np.zeros((512,512,3), np.uint8)
#img2[200:300,100:300] = 255,0,0 # taking a part of image
img2[:] = 255,0,0 # coloring whole of image

# Adding a line
img3 = np.zeros((512,512,3), np.uint8)
img3 = cv2.line(img3,(0,0),(300,300),(0,255,0), 3) # img, start pt, end pt, color, thickness
# Making the line complete
img4 = np.zeros((512,512,3), np.uint8)
img4 = cv2.line(img4,(0,0),(img4.shape[1],img4.shape[0]),(0,255,0),3) # width & height of img4

# Rectangle
img5 = cv2.line(img4,(0,0),(img4.shape[1],img4.shape[0]),(0,255,0),3)
img5 = cv2.rectangle(img5,(0,0),(250,350),(0,0,255),2)

# Circle
img6= cv2.circle(img,(400,60),35,(255,0,255),6)

# Putting Text
img7 = cv2.putText(img,"Hello World",(300,100),cv2.FONT_HERSHEY_COMPLEX,2,(250,200,100),3)

cv2.imshow("Image",img)
cv2.imshow("Image 2",img2)
cv2.imshow("Image 3",img3)
cv2.imshow("Image 4",img4)
cv2.imshow("Image 5",img5)
cv2.imshow("Image 6",img6)
cv2.imshow("Image 7",img7)

cv2.waitKey(0)


# In[7]:


import cv2
import numpy as np

#grayscale image
img = np.zeros((512,512))



# In[47]:


cv2.imshow("Image",img)
cv2.waitKey(0)


# In[53]:


img2 = np.zeros((512,512,3), np.uint8)
img2[:] = 255,0,0 # coloring whole of image
cv2.imshow("Image",img2)
cv2.waitKey(0)


# In[13]:


img3 = np.zeros((512,512,3), np.uint8)
img3 = cv2.line(img3,(0,0),(300,300),(0,255,0), 3) # img, start pt, end pt, color, thickness
cv2.imshow("Image 3",img3)
cv2.waitKey(0)


# In[19]:


# Rectangle
img4 = np.zeros((512,512,3), np.uint8)
img4 = cv2.line(img4,(0,0),(img4.shape[1],img4.shape[0]),(0,255,0),3) # width & height of img4
img5 = cv2.line(img4,(0,0),(img4.shape[1],img4.shape[0]),(0,255,0),3)
img5 = cv2.rectangle(img5,(0,0),(250,350),(0,0,255),2)
cv2.imshow("Image 5",img5)
cv2.waitKey(0)


# In[ ]:




