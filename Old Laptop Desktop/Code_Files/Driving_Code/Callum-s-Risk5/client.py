#!usr/bin/env python

# This is Callum's edition of the client code.
from imports import *
print('Imported everything')
# Arm Angles
#arm = armAngles.Arm()

# Other Vars
left_wheel_number_instructions = 0
right_wheel_number_instructions = 0 # These two variables are to ensure the robot doesn't take too many processes and lags as a result.
switchONN = True
drivername = input()
left_trigger_direction = 1
right_trigger_direction = 1 # Possible values for LB,RB = 1 (forwards), -1 (backwards) - multipliers for servo speed.
switchState = SWITCHON # Can either be off or on.

def processRHoriz(eventvalue):
    global arm
    if event.value > 0:
        if arm.hand_angle - (eventvalue/MOVEMENT_SCALING) > 0:
            arm.hand_angle -= eventvalue/MOVEMENT_SCALING 
            arm.moveJoint(HAND,arm.hand_angle,999)
        else:
            arm.hand_angle = 0
            arm.moveJoint(HAND,arm.hand_angle,100)
    else:
        if arm.hand_angle - (eventvalue/MOVEMENT_SCALING) < 1100:
            arm.hand_angle -= eventvalue/MOVEMENT_SCALING 
            arm.moveJoint(HAND,arm.hand_angle,999)
        else:
            arm.hand_angle = 1100
            arm.moveJoint(HAND,arm.hand_angle,100)

def processRVert(eventvalue):
    global arm
    if eventvalue > 0:
        if arm.shoulder_angle + 5 < 800:
            arm.shoulder_angle += 5
            arm.moveJoint(ARM,arm.shoulder_angle,999)
        else:
            arm.shoulder_angle = 800
            arm.moveJoint(ARM,arm.shoulder_angle,100)

    else:
        if arm.shoulder_angle - 5 > 200:
            arm.shoulder_angle -= 5
            arm.moveJoint(ARM,arm.shoulder_angle,999)
        else:
            arm.shoulder_angle = 200
            arm.moveJoint(ARM,arm.shoulder_angle,100)

# Uncomment this line to test the processes in the gamepad.
# gamepad = [LEFT_TRG,RIGHT_TRG,LB,RB,RHORIZ,RVERT,A,B,START]

# Main loop
print('start Main Loop')
for event in gamepad.read_loop():
    # Ensuring we have a valid instruction. event.code = 0 and event.value = 0 will fail this condition.
    if event.code != 0 or event.value != 0:
        if event.code == LEFT_TRG:
            # If it is possible to move the left wheels
            left_wheel_number_instructions = 1 if wheels.leftWheelsMove(event.value*left_trigger_direction,left_wheel_number_instructions) else left_wheel_number_instructions + 1
        elif event.code == RIGHT_TRG:
            # Move the right wheels if it can and update the number of taken instructions.
            right_wheel_number_instructions = 1 if wheels.rightWheelsMove(event.value*right_trigger_direction,right_wheel_number_instructions) else right_wheel_number_instructions + 1
        elif event.code == LB:
            if event.value > 0:
                left_trigger_direction *= -1 # Reverse the wheel turning direction
        elif event.code == RB:
            if event.value > 0:
                right_trigger_direction *= -1 # Reverse the wheel turning direction
        elif event.code == RHORIZ:
            processRHoriz(event.value)
        elif event.code == RVERT:
            processRVert(event.value)
        elif event.code == A:
            arm.slam(input()) # We need to get the password ;)
        elif event.code == B:
            wheels.switch(switchState) 
        elif event.code == START:
            left_trigger_direction, right_trigger_direction = wheels.reset()
            arm.reset()
        elif event.code == LCLICK:
            arm.increaseDecrease(SHOULDER,DECREASE)
        elif event.code == RCLICK:
            arm.increaseDecrease(SHOULDER,INCREASE)
        elif event.code == SELECT:
            print("Quitting.")
            break
    
thread1.direction = NOTHING # Being nice and giving the robot no directions when this program is finished.
