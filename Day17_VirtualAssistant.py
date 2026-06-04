import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pyjokes

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say("Hello Harsha, I am your virtual assistant. How can I help you?")
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        print("Sorry, Please say that again.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning Harsha")
    elif hour < 18:
        speak("Good Afternoon Harsha")
    else:
        speak("Good Evening Harsha")


# Start Assistant
wish_user()


while True:

    command = take_command()
    
    if "good morning" in command:
        hour = datetime.datetime.now().hour
        print(f"Current hour:{hour} AM morning")

        if hour < 12:
            speak("Good Morning")
        elif hour < 18:
            speak("It is not morning now. Good Afternoon")
        else:
            speak("It is not morning now. Good Evening")

    elif "good afternoon" in command:
        hour = datetime.datetime.now().hour
        rint(f"Current hour:{hour} PM afternoon")

        if 12 <= hour < 18:
            speak("Good Afternoon")
        elif hour < 12:
            speak("It is not afternoon now. Good Morning")
        else:
            speak("It is not afternoon now. Good Evening")

    elif "good evening" in command:
        hour = datetime.datetime.now().hour
        rint(f"Current hour:{hour} PM evening")

        if hour >= 18:
            speak("Good Evening")
        elif hour < 12:
            speak("It is not evening now. Good Morning")
        else:
            speak("It is not evening now. Good Afternoon")

    # Greetings
    elif "good morning" in command:
        speak("Good Morning Harsha")

    elif "good afternoon" in command:
        speak("Good Afternoon Harsha")

    elif "good evening" in command:
        speak("Good Evening Harsha")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Date
    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    # Open websites
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # Google Search
    elif command.startswith("search"):
        query = command.replace("search", "").strip()

        if query:
            speak(f"Searching for {query}")
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

    # Wikipedia Search
    elif "who is" in command:
        person = command.replace("who is", "").strip()

        try:
            speak(f"Searching for {person}")
            info = wikipedia.summary(person, sentences=2)

            print("\n", info)
            speak(info)

        except:
            speak("Sorry, I could not find information.")

    # Joke
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    # Help
    elif "help" in command:
        speak("""
        I can tell time,
        tell date,
        search Google,
        search Wikipedia,
        tell jokes,
        check battery,
        and open websites.
        """)

    # Exit
    elif "exit" in command or "stop" in command:
        speak("Goodbye Harsha. Have a great day.")
        break

    else:
        speak("Sorry, I don't know that command yet.")
