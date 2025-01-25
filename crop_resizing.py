import cv2
import numpy as np 

print("package import ho chuka he .. ")

img = cv2.imread("Resource/baba.jpg")

print(img.shape)  # to find height and width of an image .. 

img_resize = cv2.resize(img , (300 , 200))  # resizing .. 
img_cropped = img[0:200 , 200:450]

cv2.imshow("resized_image" , img_resize)  # imshow .. 
cv2.imshow("cropped_image" , img_cropped)

cv2.waitKey(0)