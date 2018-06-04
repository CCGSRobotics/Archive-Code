from connect import *
import lib_threading1
from constants import *

# Callum Koh's Definitions
def leftWheels(speed):
    r1 = 10000
    r2 = 30000
    speed = int(speed)

    # This line should kill the program if the speed is smaller than -1023 and larger than 1023.
    assert speed > -1024 and speed < 1024 

    # Apparently, if you press the button even a little bit, it will still roll forward. This first condition prevents this.
    if speed > -11 and speed < 11:
        r1 = str(r1)
        r2 = str(r2)
    elif speed > 10:
        r1 += speed
        r2 += speed
        r1 = str(r1)
        r2 = str(r2)
    else:
        r1 = "1-"
        r2 = "3-"
        speed = str(speed)
        
        for i in range(4-(len(speed)-1)):
            r1 += "0"
            r2 += "0"
            
        r1 += str(abs(int(speed)))
        r2 += str(abs(int(speed)))
        
    sock.sendall(bytes(r1 + "\n", "utf-8"))
    sock.sendall(bytes(r2 + "\n", "utf-8"))

def rightWheels(speed):
    r1 = 20000
    r2 = 40000
    speed = int(speed)

    # This line should kill the program if the speed is smaller than -1023 and larger than 1023.
    assert speed > -1024 and speed < 1024 

    # Apparently, if you press the button even a little bit, it will still roll forward. This first condition prevents this.
    if speed > -11 and speed < 11:
        r1 = str(r1)
        r2 = str(r2)
    elif speed > 10:
        r1 += speed
        r2 += speed
        r1 = str(r1)
        r2 = str(r2)
    else:
        r1 = "2-"
        r2 = "4-"
        speed = str(speed)
        
        for i in range(4-(len(speed)-1)):
            r1 += "0"
            r2 += "0"
            
        r1 += str(abs(int(speed)))
        r2 += str(abs(int(speed)))
        
    sock.sendall(bytes(r1 + "\n", "utf-8"))
    sock.sendall(bytes(r2 + "\n", "utf-8"))
    
# Moves the robot forward by a certain speed and an extra multiplier if neccessary. 
def leftWheelsMove(speed,number_instructions):
    if number_instructions % 5 == 0 or speed <= 0:
        # event.value seems to have a maximum value of 255 so multiplying it will meet the scaled speed of the wheels.
        leftWheels(speed * 4)
    else:
        #leftWheels(0)
        return False # If the wheels ended up not moving 
    return True # If the wheels did end up moving.

def rightWheelsMove(speed,number_instructions):
    if number_instructions % 5 == 0 or speed <= 0:
        # event.value seems to have a maximum value of 255 so multiplying it will meet the scaled speed of the wheels.
        rightWheels(-(speed * 4))
    else:
        #rightWheels(0)
        return False
    return True

def reset():
    print('Wheels reset')
    # Set the speeds to 0 and the driving direction to forward.
    leftWheelsMove(0,0)
    rightWheelsMove(0,0)
    return 1,1


def switch(state):
    if state == SWITCHON:
        sock.sendall(bytes("OFF\n", "utf-8"))
        return SWITCHOFF
    sock.sendall(bytes("ON\n", "utf-8"))
    return SWITCHON
