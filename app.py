import pyttsx3
import speech_recognition as sr
import random
import datetime
import webbrowser

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
            print(f"You said: {query}\n") 
        except Exception:
            print("Say that again please...")
        return query
    
def play_music():
    speak("Playing your favorite music.")
    
    song = random.randint(1,10)
    if song == 1:
        webbrowser.open("youtube.com/watch?v=KQtMPONdxGs&list=RDKQtMPONdxGs&start_radio=1&pp=ygUFbXVzaWOgBwE%3D")
    elif song == 2:
        webbrowser.open("https://www.youtube.com/watch?v=GX9x62kFsVU&list=RDGX9x62kFsVU&start_radio=1")
    elif song == 3:
        webbrowser.open("https://www.youtube.com/watch?v=cmMiyZaSELo&list=RDGX9x62kFsVU&index=15") 
    elif song == 4:
        webbrowser.open("https://www.youtube.com/watch?v=3EVCqRLf2Vo&list=RDGX9x62kFsVU&index=17")
    elif song == 5:
        webbrowser.open("https://www.youtube.com/watch?v=r_3K9vZ4oZE&list=RDGX9x62kFsVU&index=23")
    elif song == 6:
        webbrowser.open("https://www.youtube.com/watch?v=ru_5PA8cwkE&list=RDGX9x62kFsVU&index=27")
    elif song == 7:
        webbrowser.open("https://www.youtube.com/watch?v=Qo4IOTAbGAM&list=RDQo4IOTAbGAM&start_radio=1")
    elif song == 8:
        webbrowser.open("https://www.youtube.com/watch?v=DY1DdeW3VyI&list=RDDY1DdeW3VyI&start_radio=1")
    elif song == 9:
        webbrowser.open("https://www.youtube.com/watch?v=Qhwafoo7Pnc&list=RDQhwafoo7Pnc&start_radio=1")
    else:
        webbrowser.open("https://www.youtube.com/watch?v=xP7wxilM_4U&list=RDxP7wxilM_4U&start_radio=1")

def timeanddate(request):
    if "say time" in request:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"The current time is " + str(current_time))
    elif "say date" in request:
        now = datetime.datetime.now()
        current_date = now.strftime("%d:%m:%Y")
        speak(f"Today's date is " + str(current_date))

def TaskCreation(request):
    task = request.replace("new task", "")
    if task != "":
        speak(f"Task created: {task}")
        with open("data/tasks.txt", "a") as f:
            f.write(task + "\n")

def main():
    request = command().lower()

    if 'hello' in request:
        speak("Hello, how can I help you today?")
    elif 'play music' in request:
        play_music()
    elif 'say time' in request:
        timeanddate(request)
    elif 'say date' in request:
        timeanddate(request)
    elif 'new task' in request:
        TaskCreation(request)
        
    
if __name__ == "__main__":
    while True:
        main()
