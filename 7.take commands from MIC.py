import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir!")
    elif hour >=12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good morning sir, you are working late today!")
    
def wishme():
    speak("Welcome back sir!")
    time()
    date()
    greeting()
    speak("Jarvis at your service, please tell me how can i help you.")

def takeCommandCMD():
    query = input("please tell me how can i help you?\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:       #microphone is set to 2 as an external device because laptop mike couldnt work properly
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing......")
            query = r.recognize_google(audio,language="en-in")
            print(query)
        except Exception as e:
            print(e)
            speak("I couldn't understand what you just said, please say that again...")
            return "None"
        return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommandMIC().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
            