from PIL import ImageGrab
import cv2
import numpy as np

# manage paths
from pathlib import Path, PurePath

face_path = Path('./xmlClassifiers/haarcascade_frontalface_default.xml')
eye_path = Path('./xmlClassifiers/haarcascade_eye.xml')

# PATH TEST
#dir_list = [x for x in p.iterdir()]
#print(dir_list)


# human variables

activated = False
human_input = input("Activate system control? (Y/n) ")

if human_input == "n":
    activated = False
else:
    activated = True

print("Desktop recognition is running ...")

face_cascade = cv2.CascadeClassifier(str(face_path)) 
eye_cascade = cv2.CascadeClassifier(str(eye_path))  

def process_img(image):
    print("image processing")
    original_image = image
    print("making img gray for processing convenience")
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Canny method ")
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img


def main():

    while activated:
        screen = np.array(ImageGrab.grab(bbox=(0,40,1200,1200)))
        new_screen = process_img(screen)
        
        """
        faces = face_cascade.detectMultiScale(screen, 1.35, 5)
        for (x,y,w,h) in faces:
            
            cv2.rectangle(screen,(x,y),(x+w,y+h),(255,255,0),2)
            roi_gray = screen[y:y+h, x:x+w]
            roi_color = screen[y:y+h, x:x+w]
      
            eyes = eye_cascade.detectMultiScale(roi_gray)
      
            for (0x,0y,0w,0h) in eyes:
                cv2.rectangle(roi_color,(0x,0y),(0x+0w,0y+0h),(0,127,255),2)
        """

        cv2.imshow('img', screen)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()