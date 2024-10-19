import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print("Somthing Went Wrong, Please try again") 


        elif 'open youtube' in query:
            try:
                webbrowser.open("youtube.com")
            except Exception as e:
                print("Somthing Went Wrong, Please try again") 

        elif 'open google' in query:
            try:
                webbrowser.open("google.com")
            except Exception as e:
                print("Somthing Went Wrong, Please try again") 

        elif 'open stackoverflow' in query:
            try:
                webbrowser.open("stackoverflow.com")  
            except Exception as e:
                print("Somthing Went Wrong, Please try again") 


        elif 'play music' in query:
            try:
                USER_FOLDER = os.path.expanduser('~')
                music_dir = os.path.join(USER_FOLDER,'Music')
                files = os.listdir(music_dir)
                # Define the music file extensions you want to filter
                music_extensions = ('.mp3', '.wav', '.flac', '.aac', '.ogg')

                # Filter the list
                music_files = [file for file in files if file.endswith(music_extensions)] 
                print(music_files)    
                os.startfile(os.path.join(music_dir, music_files[0]))
            except Exception as e:
                print("Somthing Went Wrong, Please try again")
                if isinstance(e, IndexError):
                    speak("Nothing to play")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            try:
                LOCAL_APP_DATA = os.getenv('LOCALAPPDATA')
                vscodePath = os.path.join(LOCAL_APP_DATA,'Programs\\Microsoft VS Code\\Code.exe')
                os.startfile(vscodePath)
            except Exception as e:
                print("Somthing Went Wrong, Please try again")

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "some-email@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
