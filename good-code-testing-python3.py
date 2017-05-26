print("waiting")
import time
#import thread
from evdev import InputDevice, categorize, ecodes
from emuBot import *
from controller import *
'''from threading1 import *'''
try:
    from robi_camera import *
    CWorking = True
except:
    CWorking = False

print('work')

wheelMode(1)
wheelMode(2)
wheelMode(3)
wheelMode(4)

print('hello')
moveWheel(1, 100)
jointMode(5)
jointMode(6)
jointMode(7)
print("toast")
moveWheel(2,100)

def start_pos():
    defarm = [200, 200, 512]
    moveJoint(7,512,100)
    moveJoint(6,200,100)
    moveJoint(5,200,100)
    # thread1.position = 200
start_pos()
defarm = [200, 200, 512]
camerasrt = False

def LWheels(speed):
    moveWheel(1,speed)
    moveWheel(3,speed)
def RWheels(speed):
    moveWheel(4,speed)
    moveWheel(2,speed)
print("EmuBot ready...")
for event in gamepad.read_loop():
    x = event.code
    y = event.value
    z = event.type
    if x == 2:
        if y > 0:  
            LWheels(y*4)
        else:
            LWheels(0)
    elif x == 5:
        if y > 0:  
            RWheels(-(y*4))
        else:
            RWheels(0)
    elif x == 310:
        if y == 1:
            LWheels(-400)
        elif y == 0:
            LWheels(0)
    elif x == 311:
        if y == 1:
            RWheels(400)
        elif y == 0:
            RWheels(0)
    elif x == 0:
        if y > 0:
            LWheels(y/40)
            RWheels(y/40)
        elif y < 0:
                  LWheels(y/40)
                  RWheels(y/40)
    elif x == 1:
        y = event.value
        if y > 0:
            LWheels(-(y/40))
            RWheels((y/40))
        else:
            LWheels(-(y/40))
            RWheels((y/40))
    elif x == 3:
        y = event.value
        if y > 0:
            if defarm[2] - (y/4000) > 0:
               defarm[2] -= y/4000 
               moveJoint(7,defarm[2],999)
            else:
               defarm[2] = 0
               moveJoint(7,0,100)
        else:
            if defarm[2] - (y/4000) < 1100:
               defarm[2] -= y/4000 
               moveJoint(7,defarm[2],999)
            else:
               defarm[2] = 1100
               moveJoint(7,1100,100)
    elif x == 4:
        if y > 0:
            if defarm[1] + 5 < 800:
               defarm[1] += 5
               moveJoint(6,defarm[1],999)
            else:
               defarm[1] = 800
               moveJoint(6,800,100)
        else:
            if defarm[1] - 5 > 200:
               defarm[1] -= 5
               moveJoint(6,defarm[1],999)
            else:
               defarm[1] = 200
               moveJoint(6,200,100)
    elif x == 318:
        if y == 1:
            thread1.direction = "decrease"
        else:
           thread1.direction = "neutral"
    elif x == 317:
        if y == 1:
                thread1.direction = "increase"
        else:
                thread1.direction = "neutral"
    elif x == 307:
        defarm = [512,512,512]
        moveJoint(7,512,100)
        moveJoint(6,512,100)
        moveJoint(5,512,100)
        thread1.position = 512
    elif x == 308:
        defarm = [800,805,512]
        moveJoint(7,512,100)
        moveJoint(6,805,100)
        moveJoint(5,800,100)
        thread1.position = 800
    elif x == 304:
        defarm = [1000,512,512]
        moveJoint(7,512,100)
        moveJoint(6,512,100)
        moveJoint(5,1000,100)
        thread1.position = 1000
    elif x == 315:
        print('servo reset')
        start_pos()
        LWheels(0)
        RWheels(0)
        defarm = [200, 200, 512]
    elif x == 314:
        print('quiting')
        break
    elif x ==305:
        if CWorking:
            if y == 1:
                if camerasrt:
                    stopcam()
                    camerasrt = False
                else:
                    startcam()
                    camerasrt = True
    else:
        print(x)
if CWorking:
    camera.stop_preview()
start_pos()
thread1.direction = ""
moveJoint(6,512,100)

