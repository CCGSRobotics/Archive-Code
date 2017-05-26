from picamera import *
import time
camera = PiCamera()
camera.preview_fullscreen = False
camera.preview_window = (600,320,640,480)
camera.resolution = (640,480)
camera.sharpness = 10
camera.contrast = 30
camera.vflip = True
camera.hflip = True
camera.exposure_mode = "auto"
camera.brightness = 60

camera.start_preview()
#camera.stop_preview()

def startcam():
    camera.start_preview()
def stopcam():
    camera.stop_preview()
