import BasicClasses as BC

print("Arm setup")
            
class Arm:
    def __init__(self, IDs): #IDs is a array with the ids of the
                             #shoudler, tilt and pan servos in that order
        #Initiate the joints within the arm and their starting angles
        self.Shoulder = BC.Joint(IDs[0], 200)
        self.Tilt = BC.Joint(IDs[1], 200)
        self.Pan = BC.Joint(IDs[2], 512)

        #Start the threading of each joint
        self.Shoulder.start()
        self.Tilt.start()
        self.Pan.start()
        
    def MoveShoulder(self, position=None, direction=None):
        self.Shoulder.direction = direction
        self.GetAngles()
        
    def MoveTilt(self, position=None, direction=None):
        self.Tilt.direction = direction

    def MovePan(self, position=None, direction=None):
        self.Pan.direction = direction

    def MoveArmSetPos(self, ShoulderPos=None, TiltPos=None, PanPos=None):
        if ShoulderPos:
            self.Shoulder.position = ShoulderPos
        if TiltPos:
            self.Tilt.position = TiltPos
        if PanPos:
            self.Pan.position = PanPos

    def GetAngles(self):
        print('The shoulder is at position:', self.Shoulder.position)
        print('The Tilt is at position:', self.Tilt.position)
        print('The Pan is at position:', self.Pan.position)

class Flipper:
    def __init__ (self, WheelID, JointID): #ID of the seervo that controlls the flipper
        self.Joint = BC.Joint(JointID, 512)
        self.Wheel = BC.Wheel(WheelID)

        self.Joint.start()
    
    def MoveFlipper(self, direction=None):
        self.Joint.direction = direction

    def MoveWheel(self, direction=None, speed=None):
        self.Wheel.speed = speed
        self.Wheel.moveWheel()
        
        
print("Arm ready")
