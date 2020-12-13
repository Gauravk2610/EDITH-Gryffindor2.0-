import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)
    print("Recognizing")
text = r.recognize_google(audio, language= 'hi-IN')
print(text)
if 'वॉकिंग' or 'वाकिंग 'in text:
    print('Done')
