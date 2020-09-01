'''

!pip install opencv_python
     Requirement already satisfied: opencv_python in c:\users\personal\anaconda3\lib\site-packages (4.1.0.25)
     Requirement already satisfied: numpy>=1.14.5 in c:\users\personal\anaconda3\lib\site-packages (from opencv_python) (1.16.2)
!pip install opencv-contrib-python
     Requirement already satisfied: opencv-contrib-python in c:\users\personal\anaconda3\lib\site-packages (4.1.0.25)
     Requirement already satisfied: numpy>=1.14.5 in c:\users\personal\anaconda3\lib\site-packages (from opencv-contrib-python) (1.16.2)
!pip install opencv-contrib-python
     Requirement already satisfied: opencv-contrib-python in c:\users\personal\anaconda3\lib\site-packages (4.1.0.25)
     Requirement already satisfied: numpy>=1.14.5 in c:\users\personal\anaconda3\lib\site-packages (from opencv-contrib-python) (1.16.2)
'''
import cv2
import os
import numpy as np
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path="D:\\lakhan\\proj\\face1"
def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
# print image_path
#getImagesWithID(path)
    faces = []
    IDs = []
    for imagePath in imagePaths:
   #Read the image and convert to grayscale
        facesImg = Image.open(imagePath).convert('L')
        faceNP = np.array(facesImg, 'uint8')
        # Get the Label of the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # Detect the face in the image
        faces.append(faceNP)
        IDs.append(ID)
        cv2.imshow("Adding faces for training",faceNP)
        cv2.waitKey(1000)
    return np.array(IDs), faces
IDs,faces = getImagesWithID(path)
recognizer.train(faces,IDs)
recognizer.save("D:\\lakhan\\proj\\face1\\yml\\trainingdata.yml")        
cv2.destroyAllWindows()
