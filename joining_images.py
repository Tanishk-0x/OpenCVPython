import cv2 
import numpy as np 

print("package lag chuk ahe .. ")

img = cv2.imread("reference.jpg")

img_resize = cv2.resize(img , (350,250))

#------------------------------------------------------------
# to join images horizontally .. use hstack from numpy..
imghor = np.hstack((img_resize,img_resize))

# to join images vertically .. 
imgver = np.vstack((img_resize, img_resize))

#------------------------------------------------------

cv2.imshow("horizontal" , imghor)
cv2.imshow("vertical", imgver)

cv2.waitKey(0)