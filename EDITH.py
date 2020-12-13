import pyttsx3
import pyaudio
import speech_recognition as sr
from threading import Thread
import cv2
from opencv import reading
#import TFLite_detection_webcam
import keyboard
#from sample_img import main1
import wolframalpha
from pynput.keyboard import Key, Controller
import pyautogui
Key = Controller()
from TFLite_detection_webcam import walking
use = [1]
count = 0
WOLFRAMCMD = ["calculate", "joule", "newton", "news", "weather"]
read = ["reading mode"]
walk = ["walking mode", "working"]
object1 = ["object detection"]
SOS = ["save me", "help me", "emergency"]
client = wolframalpha.Client('AWAUJP-4A3PARYPYV')
try:
	engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')	
except RuntimeError:
	print('Driver fails to initialize')

voices = engine.getProperty('voices')
#print(voices)
#for voice in voices:
#    print(voice)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20-DSK')
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 130)
def voice_cmd():
    speech = sr.Recognizer()
    voice_text = ""
    print("Listening...")
    try:
        with sr.Microphone() as source:
            audio = speech.listen(source)
        voice_text = speech.recognize_google(audio, language='en-in')
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Network Error")
        speak("Network Error")
    except sr.WaitTimeoutError:
        pass
    return voice_text
def speak(cmd):
    engine.say(cmd)
    engine.runAndWait()

def key1():
    while True:
        if keyboard.is_pressed('a'):
            main()
            #t1.join()

def main():

    # voice_note = "calculate 2000 minus 127"
    voice_note = voice_cmd().lower()
    #print("Listening..")
    print("cmd: {}".format(voice_note))
    global count 
    count +=1
    if count <=1:
        t3 = Thread(target=key1)
        t3.start()
    else:
        pass
    for phrase in walk:
        if phrase in voice_note:
            print("Yes")
            speak("Ok Sir")
            print("Ok Sir")
            #main1(True, True)
            walking(False, False)
            walking(True, True)
            
    for phrase in object1:
        if phrase in voice_note:
            speak("Sure Sir")
            print("Sure Sir")
            #main1(True, True)                                                        
            #t1 = Thread(target=main1(True))
            #t1.start()
            walking(False, False)    
            walking(True)
    for phrase in read:
        if phrase in voice_note:
            reading()

    for phrase in WOLFRAMCMD:
        if phrase in voice_note:
            try:
                query = voice_note.replace('drishti ', '')
                #speak_text_cmd("Give me a minute sir")
                res = client.query(query)
                results = next(res.results).text
                speak("Give me a minute sir")
                            #speak('WOLFRAM-ALPHA says - ')
                            #speak_text_cmd('Got it.')

                print(results)
                speak(results)
            except:
                print("ERROR")
                speak("I don't know sir. Google is smarter than me")
                # webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
    for phrase in SOS:
        if phrase in voice_note:
            print("Alert Mode Activated. SOS started")
            speak("Alert Mode Activated. SOS started")
            print("Sir The Messages are been sent")
            speak("Sir The Messages are been sent")
    if 'stop' in voice_note:
        
        #t3.join()
        Key.press('q')
        Key.release('q')
        #t1.join()
        speak("Sure Sir")
    #t1.start()
if __name__ == "__main__":
    speak("Hello Sir This is Drishti.")
    # print(len(use))
    for x in range(0,len(use)):
        use.clear()
        print(use)
        speak("Do You Want to Know What can I Do")
        voice_note = 'sure'
        print("cmd: {}".format(voice_note))
        if 'yes' or 'yeah' or 'yep' or 'sure' in voice_note:
            file = open('commandlist.txt', 'r')
            f = file.readlines()
            print(f)
            speak(f)
            key1()
        else:
            pass
    #while True:
    
    
    #Emain()      
    #t3.start()
    
    #t1.join()
