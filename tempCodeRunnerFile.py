import cv2
import threading
from deepface import DeepFace


cap = cv2.VideoCapture(0)
cap.set(3 , 640)