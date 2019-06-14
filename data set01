
!pip install  opencv-python
!pip install  opencv-python
Requirement already satisfied: opencv-python in c:\users\personal\anaconda3\lib\site-packages (4.1.0.25)
Requirement already satisfied: numpy>=1.14.5 in c:\users\personal\anaconda3\lib\site-packages (from opencv-python) (1.16.2)
import cv2
​
import numpy as np
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(0)

id = input('enter user id:')
sampleN=0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        sampleN=sampleN+1
        cv2.imwrite("D:\\lakhan\\proj\\face."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(5000)
    cv2.imshow('img',img)
    cv2.waitKey(1)
    if sampleN > 25:
        break
cap.release()
cv2.destroyAllWindows()
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(0)
​
id = input('enter user id:')
sampleN=0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        sampleN=sampleN+1
        cv2.imwrite("D:\\lakhan\\proj\\face."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(5000)
    cv2.imshow('img',img)
    cv2.waitKey(1)
    if sampleN > 25:
        break
cap.release()
cv2.destroyAllWindows()
enter user id:1
       ''' after this a window will open n take 26 photos of you  '''
