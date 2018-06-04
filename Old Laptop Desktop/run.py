import subprocess
''' This Class is used to set the paths to a function of the robot, e.g. camera'''
class file:
    def __init__(self,TYPE,PATH):
        self.path = PATH
        self.type = str(TYPE)

# Enter all file paths here.
drivingPath = 'Code_Files/Driving_Code/RoboCup-2017-Driving-Code/Client-Code-2017/client.py'
cameraPath = 'path'
sensorPath = 'path'

files = [('driving',drivingPath), ('camera',cameraPath), ('sensor',sensorPath)]

print('Paths to files:')
# Loops through all the files.
for i in range(0,len(files)):
    path, t = files[i][1], files[i][0]
    
    #subprocess.run("chmod 755 " + path)
    subprocess.run("./" + path)
    print('    ' + t +' code: ' + path)
