import cv2
import os
from PIL import Image 

path = r"open cv images\slideshow images"
os.chdir(path) #change path's directory 

width = 0
height = 0
number_of_images = len(os.listdir(".")) #list all present directory  

for file in os.listdir("."):
    img = Image.open(file)
    w,h = img.size 
    width = width + w
    height = height + h
    avg_height = height / number_of_images
    avg_width = width / number_of_images
print("mean height: ", avg_height)
print("mean width: ", avg_width)
  