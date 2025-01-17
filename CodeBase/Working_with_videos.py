#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2


# In[5]:


from cv2 import (VideoCapture, imshow, waitKey,destroyAllWindows,CAP_PROP_FRAME_WIDTH,CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS)


# In[7]:


capture = VideoCapture('Videos/video_1.mp4')


# In[9]:


if not capture.isOpened():
    print("Error opening video file")

else:
    frame_width = capture.get(CAP_PROP_FRAME_WIDTH)
    frame_height = capture.get(CAP_PROP_FRAME_HEIGHT)
    fps = capture.get(CAP_PROP_FPS)

    print("image frame width:", int(frame_width))
    print("image frame height:", int(frame_height))
    print("frame rate:",int(fps))



# In[ ]:


while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Display the image frames from video file",frame)
        cv2.imshow("Grayscale",gray_frame)
        cv2.waitKey(1)

    if waitKey(25) == 27:
        break

capture.release()
destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




