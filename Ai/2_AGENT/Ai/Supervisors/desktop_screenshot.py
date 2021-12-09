from PIL import ImageGrab
import os
import cv2
import numpy as np
import time

# manage paths
from pathlib import Path, PurePath

saving_path = Path('./saved_screenshots')
face_path = Path('./xmlClassifiers/haarcascade_frontalface_default.xml')
eye_path = Path('./xmlClassifiers/haarcascade_eye.xml')

# PATH TEST
#dir_list = [x for x in p.iterdir()]
#print(dir_list)


# human variables


# timing 
initial_time = time.time()
loop_lenghts_ms = 1000
every_x_loops = 10
# ask for human feedback, interection, confronto

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
        for x in range(0, every_x_loops):

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

            x = x - 1

            if x == -1:
                cv2.imshow('img', screen)
                cv2.waitKey(4000)
                print("asking human interaction :)")
                print("Do you want me to stop? 0")
                print("Wanna save current screenshot? S|N \n" )
                combo = input("Waiting answers ... e.g. 0 S\n")

                splitted_combo = combo.split(" ")
                print(splitted_combo)


                for com in splitted_combo:
                    inted_com = int(com)
                    print(inted_com)
                    # critical if 0 is "0"
                    if int(com) == 0:
                        # activated = False
                        break
                    else:
                        print("Keep living ... ")
                        # create a personal code dictionary
                        if(com == "S"):
                            print("saving_path: ", saving_path, "deskshot_" + str(time.localtime()) + ".jpg")
                            cv2.imwrite(os.path.join(saving_path, "deskshot_" + str(time.localtime()) + ".jpg"), screen)
                
                            if cv2.waitKey(25) & 0xFF == ord('q'):
                                cv2.destroyAllWindows()

                        else:
                            end_time = time.time()
                            print("Desktop screenshot algo is shuttiding down ... used time:")
                            print("Gonna skip that, how can I help you?")




main()
