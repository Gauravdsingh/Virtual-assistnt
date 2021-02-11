import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import pyjokes
import pyowm
import pyfirmata 


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('YOUR ID HERE')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',175)
#board = pyfirmata.Arduino('COM5')

#it = pyfirmata.util.Iterator(board)
#it.start()
#board.digital[7].mode = pyfirmata.OUTPUT
#board.digital[7].write(1)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello , I am your digital assistant sam!')
speak('How may I help you?')

# 
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        return "none"
    return text


        

def workk():
        

    while True:
    
        query = takecom()
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open notepad' in query:
            speak('okay')
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        
        elif 'open cmd' in query:
            speak('okay')
            npath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(npath)

        elif 'open edge' in query:
            speak('okay')
            npath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(npath)

        elif'joke' in query or 'Tell me a joke' in query: 
            boi = pyjokes.get_joke()
            speak(boi)

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = takecom()

            if 'Gaurav' in recipient:
                try:
                    speak('What should I say? ')
                    content = takecom()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("ranjanadsingh10@gmail.com", 'mumbaikharghar')
                    server.sendmail('gauravdsingh2309@yahoo.in', "Gaurav Singh", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry ! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye , have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello ')

        elif 'sleep' in query:
            speak('OK')
            break
        
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)
        
            except:
                webbrowser.open(takecom())
        
        speak('Next Command! !')

    #while True:
     #      target = target.lower()
      #      if "on lights" in target or "turn on" in target or "wake sam" in target or "hello sam" in target:
       #        board.digital[7].write(0)
            
        #    elif "turn off" in target or "off lights" in target or "close sam" in target or "sam close" in target or "exit sam" in target or "exit" in target:
         #       board.digital[7].write(1)



    
if __name__ == '__main__':
        while True:
            permission = takecom()
            permission = permission.lower()
            if "ok sam" in permission or "ok sam" in permission or "wake sam" in permission or "hello sam" in permission:
               speak("sam Activated")
               workk()
            
            elif "goodbye sam" in permission or "bye sam" in permission or "close sam" in permission or "sam close" in permission or "exit sam" in permission or "exit" in permission:
                speak("Okay")
                sys.exit()