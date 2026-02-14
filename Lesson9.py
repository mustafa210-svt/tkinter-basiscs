#part 2 of face recognition software
#===================================
import cv2
import os 
import numpy as np 

#path variables
path = r"open cv images\face recognition"
haarfile = r"open cv images\face recognition\haarcascade_frontalface_default.xml"
facecascade = cv2.CascadeClassifier(haarfile)

images = []
labels = []
names = {}
id = 0


for (subdirectories,directories,files) in os.walk(path):  #walk function would look though everything in face recognition folder
    for directory in directories:
        names[id] = directory 
        path2 = os.path.join(path,directory)
        for file in os.listdir(path):
            imagePath = os.path.join(path2,file)
            readImage = cv2.imread(imagePath,0)
            images.append(readImage)
            labels.append(id)
        id = id + 1

(images,labels) = [np.array(lis) for lis in [images,labels]] #converting list into array for faster excution 
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
print("model trained succesfuly ")
video = cv2.VideoCapture(0)
while True:
    (_,im) = video.read()
    if _ == False:
        continue

    greyscale = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(greyscale,1.3,3)
    #spotting the faces
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(im,(x,y),(x+w,y+h),color= "Red",thickness= 3)
        face = greyscale[x:x+w, y:y+h]
        resizeFace = cv2.resize(face,(130,100))
        prediction1,prediction2 = model.predict(face)
        if prediction2 < 500:
            text = "Found" + {prediction1}
            color = "black"
            thickness = 3
            fontstyle = cv2.FONT_HERSHEY_DUPLEX
            fontscale = 3
            topleft = 80

            cv2.putText(face,text,topleft,fontstyle,fontscale,color,thickness)
           
            
    cv2.imshow("face picture",face)
    cv2.waitKey(0)
            

       

            
    
    
