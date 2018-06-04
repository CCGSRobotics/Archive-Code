import threading

print("threading setup")

# Class is deprecated because threads can be initialised with threading.Thread() and these functions can be used in the arm class.
"""
class ShoulderMovement(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.direction = NEUTRAL
        self.position = 200 # angle/position of the servo
        
    def run(self):
        while self.direction != NOTHING:
            if self.direction == DECREASE and self.position > 200:
                self.position -= 10
            elif self.direction == INCREASE and self.position < 1000:
                self.position += 10
                
            if self.direction != NEUTRAL:
                arm.moveJoint(SHOULDER,self.position,900)

            # Alternative code to handle broken pipe errors
            '''try:
                moveJoint(5,self.position,200)
            except (BrokenPipeError, IOError):
                #print("Broken pipe error caught")
                pass'''
            time.sleep(0.08)
"""            
            

thread1 = threading.Thread()
thread1.start()
print("threading ready")
