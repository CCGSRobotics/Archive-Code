import threading
import time
from emuBot import *

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.direction = "netural"
        self.position = int(200)
    def run(self):
        while self.direction != "":
            if self.direction == "decrease":
                if self.position > 200:
                    self.position -= 10
            elif self.direction == "increase":
                if self.position < 1000:
                    self.position += 10
            moveJoint(5,int(self.position),200)
            time.sleep(0.08)

thread1 = myThread()
thread1.start()
