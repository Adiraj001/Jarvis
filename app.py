import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    query = ""
    while query == "":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
        return query

def main():
    request = command().lower()
    if 'hello' in request:
        speak("Hello, how can I help you today?")

