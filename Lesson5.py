import cv2
import numpy as np

#hough circle detection algorithim 
cr_image = cv2.imread(r"open cv images\circles.png",cv2.IMREAD_COLOR) 
Gray_cr = cv2.cvtColor(cr_image, cv2.COLOR_BGR2GRAY)
gaussian_cr = cv2.GaussianBlur(Gray_cr,(3,3), 0)    
circles = cv2.HoughCircles(gaussian_cr,cv2.HOUGH_GRADIENT,1.2,50,param1= 100,param2= 30,minRadius=  10, maxRadius= 40)
if circles is not None:
    circles = np.uint16(np.around(circles)) 
    for pt in circles[0,:]:
        a,b,r = pt
        thickness = 15
        color = 50,50,250
        circle = cv2.circle(cr_image,(a,b), r, color,thickness)
        cv2.circle(cr_image,(a,b),1,(255,0,0),10)
        cv2.imshow("highlighted circle",cr_image)
        #Wait and destroy
        cv2.waitKey(0)


cv2.destroyAllWindows()





