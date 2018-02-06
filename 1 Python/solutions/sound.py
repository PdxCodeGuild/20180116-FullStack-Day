import math  # import needed modules
import pyaudio  # sudo apt-get install python-pyaudio

PyAudio = pyaudio.PyAudio  # initialize pyaudio

# See https://en.wikipedia.org/wiki/Bit_rate#Audio
bitrate = 16000  # number of frames per second/frameset.

frequency = 261.63  # Hz, waves per second, 261.63=C4-note.
length = 1  # seconds to play sound

if frequency > bitrate:
    bitrate = frequency + 100

n_frames = int(bitrate * length)
rest_frames = n_frames % bitrate
wavedata = ''


for x in range(n_frames):
    wavedata += chr(int(math.sin(x / ((bitrate / frequency) / math.pi)) * 127 + 128))

for x in range(rest_frames):
    wavedata += chr(128)

p = PyAudio()
stream = p.open(format=p.get_format_from_width(1),
                channels=1,
                rate=bitrate,
                output=True)

stream.write(wavedata)
stream.stop_stream()
stream.close()
p.terminate()
