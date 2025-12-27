# 🤖 Jarvis – Python Voice Assistant

Jarvis is a Python-based voice assistant designed to perform daily tasks using voice commands. It listens through your microphone, processes speech, and responds with natural voice output while automating common system and web-based actions.

---

## 🚀 Features

* 🎙️ Voice recognition using microphone
* 🔊 Text-to-speech responses
* 🎵 Play random music on YouTube
* 🕒 Speak current time and date
* 📝 Task management (add, read, clear tasks)
* 🔔 Desktop notifications for tasks
* 🌐 Google and YouTube search
* 📚 Wikipedia information lookup
* 🖥️ Open applications using voice
* 🔐 System controls (lock, shutdown, restart)
* ❌ Exit assistant via voice command

---

## 🧠 How It Works

1. Listens to user voice input via microphone
2. Converts speech to text
3. Matches commands with predefined actions
4. Executes tasks and responds using text-to-speech

---

## 🛠️ Technologies Used

* Python 3
* SpeechRecognition
* Pyttsx3 (Text-to-Speech)
* PyAudio
* PyAutoGUI
* Wikipedia API
* Plyer (Notifications)

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ **Important (Windows Users):**
> If `pyaudio` fails to install, download the compatible `.whl` file from:
> [https://www.lfd.uci.edu/~gohlke/pythonlibs/](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

---

## ▶️ Run the Assistant

```bash
python Jarvis.py
```

You will hear:

> **"Jarvis is now online."**

---

## 🗣️ Sample Voice Commands

| Command                 | Description            |
| ----------------------- | ---------------------- |
| Hello / Hi              | Greets the user        |
| Play music              | Plays music on YouTube |
| Say time                | Speaks current time    |
| Say date                | Speaks today’s date    |
| Add task buy milk       | Adds a task            |
| Speak task              | Reads saved tasks      |
| Clear tasks             | Deletes all tasks      |
| Open Chrome             | Opens application      |
| Search Python tutorials | Google search          |
| Search YouTube songs    | YouTube search         |
| Wikipedia Elon Musk     | Wikipedia summary      |
| Lock computer           | Locks system           |
| Shutdown system         | Shuts down PC          |
| Restart system          | Restarts PC            |
| Exit / Bye              | Stops Jarvis           |

---

## 📁 Project Structure

```
├── Jarvis.py
├── tasks.txt
├── requirements.txt
├── README.md
```

---

## ⚠️ Limitations

* Requires an active internet connection for:

  * Speech recognition
  * Wikipedia
  * Web searches
* System commands are **Windows-only**
* No wake word detection (always listening)

---

## 🔮 Future Enhancements

* Wake word support (e.g., “Hey Jarvis”)
* GUI or web dashboard
* AI-powered responses
* Cross-platform system control
* Offline speech recognition

---

## 👨‍💻 Author

**Aditya Raj Pandey**
