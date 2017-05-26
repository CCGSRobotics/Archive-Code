from pyax12.connection import Connection
import time
sc = Connection(port="/dev/ttyACM0", baudrate=57600, timeout=0, waiting_time=0.01)
ids = sc.scan()

print((ids))
for id in ids:
    print(id)
sc.close()
