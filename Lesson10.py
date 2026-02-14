#====================
#Car detection system
#====================


#imorting libraries 
import cv2
import numpy as np

#variables 
video = cv2.VideoCapture(r"open cv images\Car detection\Cars.mp4")
haarfile =r"open cv images\Car detection\cars.xml"
car_cascade = cv2.CascadeClassifier(haarfile)


while (video.isOpened):
    rv,images = video.read()
    if rv == False:
        continue

    greyscale = cv2.cvtColor(images,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(greyscale)
    for car in cars:
        x,y,w,h = car
        cv2.rectangle(images,(x,y),(x+w,y+h), color = (0,0,250),thickness= 2)
        
    
    cv2.imshow("Cars",images)
    key = cv2.waitKey(10)
    if key == 27:
        break





    

