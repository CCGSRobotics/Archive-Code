# pyaudio callback server

import pyaudio, time, socket
from constants import *

player = AudioPlayer(CHUNK_SIZE, WIDTH, RATE, CHANNELS)

s = socket.socket()
s.bind(("",PORT))

print("Audio server is working alright so far.")
s.listen(1)
client, address = s.accept()

print("Connection from: " + str(address))

while True:
    #print(client.recv(8192))
    data = client.recv(4096)
    print(len(data))
    if not data:
        break
    
    #print("From connected user: " + data)
    player.audioData = data
    player.play()
    #time.sleep(0.0001)

client.close()
player.close()
