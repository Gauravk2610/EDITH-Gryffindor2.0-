import pyaudio
from threading import Thread
import pyttsx3

try:
	engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')	
except RuntimeError:
	print('Driver fails to initialize')

voices = engine.getProperty('voices')
print(voices)
for voice in voices:
    print(voice)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20-DSK')
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 160)
def speak(cmd):
    engine.say(cmd)
    engine.runAndWait()
# Data = []

#loop = False
def speaking(data):
    if bool(data):

        speak(data)

lis=[["Hi, Ravi !",0]]

def talk(lis):
    engine = pyttsx3.init()
    for x in lis:
        if x[1]==0:
            engine.say(x[0])
            engine.runAndWait()
            x[1]=1

def delay():
    ini=time.time()
    while True:
        final=time.time()
        s=final-ini
        if s>=3:
            print(s)
            break


# t1 = threading.Thread(target=talk, args=(lis,))

# t1.start()
# print(lis)
# delay()
# lis.append(["Hi, Swara !",0])
# delay()
# print(lis)
# lis.append(["Hi, Pranay !",0])
# t1.join()
# print(lis)
# # both threads completely executed 
# print("Done!") 