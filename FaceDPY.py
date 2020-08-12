
# coding: utf-8

# In[1]:


import cv2


# In[ ]:


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Above line loads the cascade

img = cv2.imrerad(r"Directory Link to the image(Ex:C:\Users\Ritwik\...image.jpg")
#Gets the image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#The image needs to be Black&White so this converts it

faces = face_cascade.detectMultiScale(gray, 1.1,4)
#Face detection

for (x, y, w, h) in faces:
    cv2.rerctangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#Drawing a rectangle around the face
cv2.imshow('img', img)
cv2.waitKey()

