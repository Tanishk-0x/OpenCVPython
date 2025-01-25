import cv2 
import numpy as np 

print("package import ho chuka he .. ")

img = np.zeros((512 , 512 , 3),np.uint8) 

# print(img)

# img[:]= 255 , 0 , 0 # to colour the image ...
 
#--------------------------------------------------------------------------------
#  how to draw shapes .. 
cv2.line(img , (0,0),(300,300),(0,255,0),3)  # to draw line .. 
cv2.rectangle(img ,(0,0),(250,350),(0,0,255),5 )  # to draw rectangle .. 
cv2.circle(img,(400,50),30,(255,255,0),7)  # to draw circle ..
# use cv2.filled to fill the image 

#-----------------------------------------------------------------------------------

# how to put text .. 
cv2.putText(img , "text to display ",(280,200),cv2.FONT_HERSHEY_COMPLEX , 1 ,(0 , 150 , 0 ) , 2)


#-----------------------------------------------------------------------------------


cv2.imshow("image" , img)
cv2.waitKey(0)