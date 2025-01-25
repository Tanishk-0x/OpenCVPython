import cv2 
import numpy as np 

print(" package import ho chuka he ")

img = cv2.imread("Resource/card.jpg")
img_resize = cv2.resize(img,(350,230))

#-----------------------------------------------
# warp perspective .. 

width,height = 250 , 350 
point1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
point2 = np.float32([[0,0],[width,0],[height,0],[width,height]])
matrix = cv2.getPerspectiveTransform(point1 , point2)
img_output = cv2.warpPerspective(img , matrix , (width , height))



cv2.imshow("output" , img_resize)
cv2.imshow("image_output" , img_output)
cv2.waitKey(0)