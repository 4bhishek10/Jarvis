import pyttsx3
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getVoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
    
    if voice == 2:
        engine.setProperty('voice',voices[1].id) 
    
    speak("Hello this is jarvis")

while True:
    voice = int(input("Press 1 for Female voice\n Press 2 for male voice\n"))
    getVoices(voice)

