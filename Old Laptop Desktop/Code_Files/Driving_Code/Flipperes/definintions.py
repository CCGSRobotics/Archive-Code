from connect import *
print("definitions setup")

def SwitchON():
   sock.sendall(bytes("ON\n", "utf-8"))
def SwitchOFF():
    sock.sendall(bytes("OFF\n", "utf-8"))


print("definitions made")
