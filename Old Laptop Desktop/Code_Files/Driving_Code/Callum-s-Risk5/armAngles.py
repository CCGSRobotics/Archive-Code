# Arm Angles Class
import lib_threading1
from constants import *
from connect import *

class Arm:
    def __init__(self):
        self.shoulder_angle = 200
        self.arm_angle = 200
        self.hand_angle = 512

        self.moveJoint(HAND,self.hand_angle,100)
        self.moveJoint(ARM,self.arm_angle,100)
        self.moveJoint(SHOULDER,self.shoulder_angle,100)
    
    def moveJoint(self,ID, position, speed):
        position = int(position)
        speed = int(speed)
        
        while len(str(speed)) < 4:
            speed = "0" + str(speed)
            
        while len(str(position)) < 4:
            position = "0" + str(position)
            
        sock.sendall(bytes(str(ID) + str(position) + str(speed) + "\n", "utf-8"))
    
    def slam(self,passwd):
        if passwd == "01123581321":
            self.shoulder_angle = 1000
            self.arm_angle = self.hand_angle
            self.hand_angle = 1023
            
            self.moveJoint(HAND,self.hand_angle,999)
            self.moveJoint(ARM,self.hand_angle,999)
            self.moveJoint(SHOULDER,self.shoulder_angle,999)
            thread1.position = 1000
            
    def ArmUp(self):
        self.shoulder_angle = 512
        self.arm_angle = 512
        self.hand_angle = 512
        
        self.moveJoint(HAND,self.hand_angle,100)
        self.moveJoint(ARM,self.arm_angle,100)
        self.moveJoint(SHOULDER,self.shoulder_angle,100)
        
        thread1.position = 512

    
    def ArmForwards(self):
        self.shoulder_angle = 800
        self.arm_angle = 805
        self.hand_angle = 512
        
        self.moveJoint(HAND,self.hand_angle,100)
        self.moveJoint(ARM,self.arm_angle,100)
        self.moveJoint(SHOULDER,self.shoulder_angle,100)

        thread1.position = 800

    def reset(self):
        print("Arm servos reset")
        self.shoulder_angle = 200
        self.arm_angle = 200
        self.hand_angle = 512
    
    # Experimental function, just in case it is needed.
    def updateAngles(self,shoulder_angle,arm_angle,hand_angle):
        self.shoulder_angle = shoulder_angle
        self.arm_angle = arm_angle
        self.hand_angle = hand_angle
        
    def increaseDecrease(self,ID,operator): # Operator is either INCREASE or DECREASE
        if ID == HAND:
            if operator == INCREASE:
                self.hand_angle += 10
            elif operator == DECREASE:
                self.hand_angle -= 10
        elif ID == SHOULDER:
            if operator == INCREASE and shoulder_angle < 1000:
                self.shoulder_angle += 10
            elif operator == DECREASE and shoulder_angle > 200:
                self.shoulder_angle -= 10
        elif ID == ARM:
            if operator == INCREASE:
                self.arm_angle += 10
            elif operator == DECREASE:
                self.arm_angle -= 10
            
                
        
