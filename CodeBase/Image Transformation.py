#!/usr/bin/env python
# coding: utf-8

# In[22]:


from PIL import Image
import PIL
from PIL import Image 
from PIL import ImageFont 
from PIL import ImageDraw 

# creating a image object (main image)
im1 = Image.open(r"C:\Users\Nishanth\Documents\Pictures\pic1.jpg")
im1.show()
# rotating a image 90 deg counter clockwise
im1 = im1.rotate(90, PIL.Image.NEAREST, expand = 1)

# Flip the original image vertically
vertical_img = im1.transpose(method=Image.FLIP_TOP_BOTTOM)
#vertical_img.save("vertical.png")

vertical_img.show()

# Write Texts on Images 
draw = ImageDraw.Draw(im1) 
  
# specifying coordinates and colour of text 
draw.text((50, 90), "MonaLisa ", (255, 255, 255)) 

# to show specified image
im1.show()


# In[ ]:




