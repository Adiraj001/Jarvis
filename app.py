import pyttsx3
import speech_recognition as sr
import random
import datetime
import webbrowser
import sys
import os

engine = pyttsx3.init()
engine.setProperty('rate', 200)

def speak(audio):
    print(f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n") 
        return query.lower()
    except Exception:
        return ""
    
def play_music():
    speak("Playing your favorite music.")
    links = [
        "youtube.com/watch?v=KQtMPONdxGs&list=RDKQtMPONdxGs",
        "https://www.youtube.com/watch?v=GX9x62kFsVU",
        "https://www.youtube.com/watch?v=cmMiyZaSELo",
        "https://www.youtube.com/watch?v=3EVCqRLf2Vo",
        "https://www.youtube.com/watch?v=r_3K9vZ4oZE",
        "https://www.youtube.com/watch?v=ru_5PA8cwkE",
        "https://www.youtube.com/watch?v=Qo4IOTAbGAM",
        "https://www.youtube.com/watch?v=DY1DdeW3VyI",
        "https://www.youtube.com/watch?v=Qhwafoo7Pnc",
        "https://www.youtube.com/watch?v=xP7wxilM_4U"
    ]
    webbrowser.open(random.choice(links))

def timeanddate(request):
    now = datetime.datetime.now()
    if "time" in request:
        current_time = now.strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in request:
        current_date = now.strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

def TaskCreation(request):
    
    if not os.path.exists("data"):
        os.makedirs("data")

    if "new task" in request:
        task = request.replace("new task", "").strip()
        if task:
            with open("data/tasks.txt", "a") as f:
                f.write(task + "\n")
            speak(f"Added to your list: {task}")
        else:
            speak("What is the task you'd like to add?")
            
    elif "speak task" in request:
        try:
            with open("data/tasks.txt", "r") as f:
                tasks = f.readlines()
                if tasks:
                    speak("Here are your tasks:")
                    for task in tasks:
                        speak(task.strip())
                else:
                    speak("Your task list is empty.")
        except FileNotFoundError:
            speak("You have no tasks saved yet.")

def main():
    request = command()

    if not request:
        return 

    if 'hello' in request:
        speak("Hello, how can I help you today?")
    
    elif 'play music' in request:
        play_music()
    
    elif 'say time' in request or 'say date' in request:
        timeanddate(request)
    
    elif 'new task' in request or 'speak task' in request:
        TaskCreation(request)
    
    elif 'exit' in request or 'quit' in request or 'bye' in request:
        speak("Goodbye!")
        sys.exit()

if __name__ == "__main__":
    speak("Jarvis is now online.")
    while True:
        main()