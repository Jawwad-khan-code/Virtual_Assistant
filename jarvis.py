import pyttsx3
import datetime
import speech_recognition as sr
#import PyAudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # to get voices.
# print(voices[1].id)# to print the voices available.
engine.setProperty('voice', voices[0].id)  # to set voice.


def wishme():
    # time is converted into int from 0 t0 24.
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")

    speak("I am your robot sir, how may i help u")


def speak(audio):

    engine.say(audio)  # engine would speak.
    engine.runAndWait()


def takecommand():
    # it takes microphone input and returns string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1  # time of the interval between speaking.
        audio = r.listen(source)
    try:
        print("Recognising")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please")
        return "None"
    return query


if __name__ == '__main__':
    wishme()  # calling the wishme function.
    query = takecommand().lower()  # coverts the query string into lower case.
    # logic for executing task based on the query
    if 1:

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")

        elif 'open code' in query:
            code_path = "C:\\Users\Atif Khan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
