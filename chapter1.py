import cv2
import numpy as np 

print("package lag chuka he .. ")


#--------------------------------------------------
# img ko read kese kare .. 

# img = cv2.imread("Resource/baba.jpg")
# cv2.imshow("output" , img )
# cv2.waitKey(0)


#-------------------------------------------------
# video ko read kse kare .. 
# cap = cv2.VideoCapture("Resource/lambo.mp4")
# cap.set(3 , 640)
# cap.set(4 , 480)


# while True:
#     success, img = cap.read() 
#     cv2.imshow("video" , img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'): 
#         break 

#-----------------------------------------------------
cap = cv2.VideoCapture(0)
cap.set(3 , 640)
cap.set(4 , 480)
cap.set(10, 100 )  # brightness .. 

while True:
    success, img = cap.read() 
    cv2.imshow("video" , img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): 
        break


#---------------------------------------------------
# img ke effects .. 

# img = cv2.imread("Resource/baba.jpg")

# imggray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imggray , (7,7),0)
# imgcanny = cv2.Canny(img ,100,100)

# cv2.imshow("gray_image" , imggray)
# cv2.imshow("blur_image" , imgblur)
# cv2.imshow("canny_image" , imgcanny)
# cv2.waitKey(0)

#--------------------------------------------------
# dialated image .. 

# img = cv2.imread("Resource/baba.jpg")
# kernel = np.ones((5,5),np.uint8)

# canny = cv2.Canny(img , 100 , 100)
# imgdailation = cv2.dilate(canny , kernel , iterations=1)
# imageerode = cv2.erode(imgdailation , kernel , iterations=1)

# cv2.imshow("canny_img" , canny)
# cv2.imshow("dilated_img" , imgdailation)
# cv2.imshow("eroded_img" , imageerode)
# cv2.waitKey(0)

#----------------------------------------------------------