# TCP Constants
import pyaudio

RATE = 48000
CHANNELS = 2
CHUNK_SIZE = 1024
WIDTH = pyaudio.paInt32

HOST = "127.0.0.1" #"192.168.100.1" this host can pretty much be almost anything as long as it is the same IP as the one on the pi.
PORT = 12024

class AudioPlayer:
    """ Plays a single chunk of audio data """ 
    def __init__(self, chunksize, width, rate, channels):
        """ Init audio stream """ 
        self.p = pyaudio.PyAudio()

        self.audioData = "" # This is mutable
        self.chunksize = chunksize
        self.width = width
        self.rate = rate
        self.channels = channels

        self.stream = self.p.open(
            format = self.width,
            channels = self.channels,
            rate = self.rate,
            output = True
        )

    def play(self):
        """ Play entire BYTE STRING """
        self.stream.write(self.audioData)
        
    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()
