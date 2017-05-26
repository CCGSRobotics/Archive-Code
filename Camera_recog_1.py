from picamera.array import PiRGBArray
from picamera import PiCamera
import time
#import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array
for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
    image = frame.array

    cv2.imshow("Frame",image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
#cv2.imshow("Image",image)
#cv2.waitKey(0)
time.sleep(1)
