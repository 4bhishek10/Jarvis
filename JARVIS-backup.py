import pyttsx3
import datetime
import pyaudio
import smtplib
import pyautogui
import wikipedia
import pywhatkit
import os
from newsapi import NewsApiClient
import webbrowser as wb
from time import sleep
from secrets import senderEmail, epwd, to
import speech_recognition as sr


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',196)                   #talking speed of jarvis


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getVoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak("Hello this is Friday")
    
    if voice == 2:
        engine.setProperty('voice',voices[2].id)
        speak("Hello this is jarvis")
    
    

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

def sendEmail(content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sendEmail, epwd)
    server.sendmail(sendEmail, to, content)
    server.close()

def sendWhatMsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(20)
    pyautogui.press('enter')

def shopOnline(search):
    keyword = search
    wb.open('https://www.amazon.in/s?k='+keyword)
    wb.open('https://www.flipkart.com/search?q='+keyword)

def searchGoogle():
    speak("what should i search for?")
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key='b9efcd92e576480fba0a5cd149df2b30')
    speak("What topic you want news updates on?")
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q = topic, language = 'en', page_size = 5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    speak("Thats it for now, I will update you later.")

def SpeedTest():
    import speedtest
    speak("checking the speed......")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUp = int(uploading/800000)
    speak("Sir your downloading speed is "+str(correctDown)+"M b p s")
    speak("and your uploading speed is "+str(correctUp)+"M b p s")



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
    #getVoices(2)                                       #2 for male voice
    #wishme()
    while True:
        query = takeCommandMIC().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        
        elif 'how are you' in query:
            speak("i am fine, what about you?")

        elif 'i am fine' in query:
            speak("good to hear")

        elif 'thank you' in query:
            speak("at your service sir!")
        
        elif 'email' in query:
            try:
                speak("What should i say?")
                content = takeCommandMIC()
                sendEmail(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("unable to send the email")

        elif 'friday version' in query:
            getVoices(1)

        elif 'jarvis version' in query:
            getVoices(2)

        elif 'message' in query:
            user_name = {
                'friend' : '+91 8793420998',
                'mother' : '+91 9922745117',
                'father' : '+880 1777-641241'
            }
            try:
                speak("To Whom you want to send the whats app message?")
                name = takeCommandMIC()
                phone_no = user_name[name]
                speak("What is the message?")
                message = takeCommandMIC()
                sendWhatMsg(phone_no, message)
                speak("meassage has been sent.")
            except Exception as e:
                print(e)
                speak("unable to send the whats app message")  

        elif 'wikipedia' in query:
            # use "wikipedia about" to search on wiki
            speak("serching on wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'shop online' in query:
            try:
                speak("What are you looking for?")
                search = takeCommandMIC().lower()
                shopOnline(search)
                speak("Here are some results")
            except Exception as e:
                print(e)
                speak("Unable to find the product")

        elif 'search' in query:
            searchGoogle()

        elif 'youtube' in query:
            speak("What should i search for on youtube?")
            topic = takeCommandMIC()
            pywhatkit.playonyt(topic)

        elif 'news' in query:
            news()

        elif 'i need to code' in query:
            speak("ok, opening Microsoft Vs code...")
            path = 'H:\\Microsoft VS Code\\Code.exe'
            os.startfile(path)

        elif 'remember that' in query:
            speak("What should i remember?")
            data = takeCommandMIC()
            speak("you asked me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you told me to remember that"+remember.read())

        elif 'internet speed' in query:
            SpeedTest()

        elif 'offline' in query:
            speak("Going offline, have a nice day sir")
            quit()    