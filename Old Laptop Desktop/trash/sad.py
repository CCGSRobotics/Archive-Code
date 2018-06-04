import cv2
import numpy as np

img = cv2.imread('cam.jpg',1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([169,100,100],dtype=np.uint8)
upper = np.array([189,255,255],dtype=np.uint8)

mask = cv2.inRange(hsv,lower,upper)

cv2.imshow('mask',mask)
cv2.imshow('image',img)
