from abc import get_cache_token
import numpy as np
import cv2





def face_detector():
    face_cascade = cv2.CascadeClassifier('C:/Users/N/Desktop/haarcascade_frontalface_default.xml')
    
    image = cv2.imread('C:/Users/N/Desktop/test.jpg')
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(grayImage)
    
    print(type(faces))
    
    if len(faces) == 0:
        print("No faces found")
    
    else:
        print(faces)
        print(faces.shape)
        print("Number of faces detected: " + str(faces.shape[0]))
    
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
    
        cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
        cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
    
        cv2.imshow('Image with faces',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

imagine to create everything with a get_cache_token

then you got to 


CLASSIFY

1 or 0

and brain frequency
emotions?



sony experiment

        