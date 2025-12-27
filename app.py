import pyttsx3
import speech_recognition as sr
import random
import datetime
import webbrowser
import sys
import os
from plyer import notification
import pyautogui
import wikipedia
import subprocess
import platform
import ctypes

def speak(audio):
    print(f"Jarvis: {audio}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 180) 
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except Exception:
            return ""

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n") 
        return query.lower()
    except Exception:
        return ""
    
def play_music():
    speak("Playing your favorite music.")
    links = [
        "https://www.youtube.com/watch?v=KQtMPONdxGs",
        "https://www.youtube.com/watch?v=GX9x62kFsVU",
        "https://www.youtube.com/watch?v=cmMiyZaSELo",
        "https://www.youtube.com/watch?v=NvSt5Nsmxlg&list=RDNvSt5Nsmxlg&start_radio=1",
        "https://www.youtube.com/watch?v=KIzCpTA2p5Y&list=RDKIzCpTA2p5Y&start_radio=1",
        "https://www.youtube.com/watch?v=DY1DdeW3VyI&list=RDDY1DdeW3VyI&start_radio=1",
        "https://www.youtube.com/watch?v=Qo4IOTAbGAM&list=RDIGti1RTS1wc&index=2"
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

    if "new task" in request or "add task" in request:
        task = request.replace("new task", "").replace("add task", "").strip()
        if not task:
            speak("What is the task you'd like to add?")
            task = command()
        if task:
            with open("data/tasks.txt", "a") as f:
                f.write(task + "\n")
            speak(f"Added to your list: {task}")
            
    elif "speak task" in request:
        try:
            if os.path.exists("data/tasks.txt"):
                with open("data/tasks.txt", "r") as f:
                    tasks = f.readlines()
                    if tasks:
                        speak("Here are your tasks:")
                        for task in tasks:
                            speak(task.strip())
                    else:
                        speak("Your task list is empty.")
            else:
                speak("You have no tasks saved yet.")
        except Exception:
            speak("I had trouble reading your tasks.")

def clear_tasks():
    file_path = "data/tasks.txt"
    if os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("") 
        speak("I have cleared all your tasks.")
    else:
        speak("You don't have a task list to clear.")

def system_control(request):
    if "lock" in request:
        speak("Locking your computer.")
        ctypes.windll.user32.LockWorkStation()

    elif "shutdown" in request:
        speak("Shutting down the computer in 10 seconds. Make sure to save your work.")
        os.system("shutdown /s /t 10")

    elif "restart" in request:
        speak("Restarting the computer.")
        os.system("shutdown /r /t 10")
        
    elif "cancel" in request or "abort" in request:
        os.system("shutdown /a")
        speak("The shutdown sequence has been cancelled.")

def open_application(request):
    query = request.replace("open", "").strip()
    speak(f"Opening {query}")
    pyautogui.press("super")
    pyautogui.typewrite(query)
    pyautogui.sleep(2)
    pyautogui.press("enter")

def show_notification():
    if os.path.exists("data/tasks.txt"):
        with open("data/tasks.txt", "r") as f:
            task = f.read()
        notification.notify(
            title="Your Tasks",
            message=task if task else "No tasks found",
            timeout=10
        )
    else:
        speak("No tasks to show.")

def wikipedia_search(request):
    speak("Searching Wikipedia...")
    query = request.replace("wikipedia", "").replace("search", "").replace("jarvis", "").strip()
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(result)
    except Exception:
        speak("I couldn't find any information on that topic.")

def google_search(request):
    query = request.replace("search", "").replace("jarvis", "").strip()
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def youtube_search(request):
    query = request.replace("search youtube", "").replace("jarvis", "").strip()
    speak(f"Searching YouTube for {query}")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def main():
    request = command()

    if not request:
        return 

    if 'hello' in request or 'hi' in request:
        speak("Hello, how can I help you today?")
    
    elif 'play music' in request:
        play_music()
    
    elif 'say time' in request or 'say date' in request:
        timeanddate(request)
    
    elif 'new task' in request or 'speak task' in request or 'add task' in request:
        TaskCreation(request)
    
    elif 'exit' in request or 'quit' in request or 'bye' in request:
        speak("Goodbye!")
        sys.exit()

    elif 'show work' in request or 'so task' in request or 'so work' in request:
        show_notification()
        
    elif "open" in request:
        open_application(request)

    elif "wikipedia" in request:
        wikipedia_search(request)

    elif "search youtube" in request:
        youtube_search(request)

    elif "search" in request:
        google_search(request)
    
    elif 'clear task' in request or 'delete tasks' in request:
        clear_tasks()

    elif 'lock' in request or 'shutdown' in request or 'restart' in request:
        system_control(request)

if __name__ == "__main__":
    speak("Jarvis is now online.")
    while True:
        main()