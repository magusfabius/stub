
import os
import cv2
import time

url = "https://en.wikipedia.org/wiki/Jack_Sparrow#/media/File:Jack_Sparrow_In_Pirates_of_the_Caribbean-_At_World's_End.JPG"

def get_image(url):



def show_image(pause):
    img = cv2.imread("flowers.jpg")

    cv2.imshow("Flowers",img)
    initial_time = time.time()

    cv2.waitKey(3000)
    final_time = time.time()

    print("Window is closed after",(final_time-initial_time))