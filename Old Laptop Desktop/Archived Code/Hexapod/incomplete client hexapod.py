#!/usr/bin/env python
import time
from controller import *
#from connect import *
print("controller ready")



def start_pos():
    defarm = [200, 200, 512]
    moveJoint(7,512,100)
    moveJoint(6,200,100)
    moveJoint(5,200,100)
    thread1.position = 200

defarm = [200, 200, 512]

Li = 0
Ri = 0
ForwardsI = 0

SwitchONN = True
alf = ""
backwardsl = 1
backwardsr = 1

from lib_threading1 import *
print("Vroom Vroom!")
for event in gamepad.read_loop():
    try:
        x = event.code
        y = event.value
        z = event.type
        
    except BrokenPipeError as e:
        print(e)

thread1.direction = ""
