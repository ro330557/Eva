import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import os
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

sorry_responses = [
    "I'm sorry, I didn't catch that. Could you please repeat?",
    "Oops, it seems I'm having trouble understanding. Can you say that again?",
    "My apologies, I didn't get that. Could you try restating your command?",
]

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_user_name(command):
    # Extract the user's name from the command more accurately
    name_start_index = command.find("i am") + len("i am")
    name_end_index = command.find(" ", name_start_index)
    
    if name_start_index != -1 and name_end_index != -1:
        user_name = command[name_start_index:name_end_index].strip()
        return user_name
    else:
        return None

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            
            if "eva" in command:
                command = command.replace("eva", "").strip()
                print(command)
            return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    
def open_chrome():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  
    if os.path.exists(chrome_path):
        os.startfile(chrome_path)
    else:
        print("Application not found")

def run_eva():
    command = take_command()
    print(command)
    
    # PERSONAL COMMANDS
    if "how are you" in command:
        talk("I'm fine.")
        print("I'm fine.")
        
    elif "are you single" in command:
        talk("Right now my relationship status is single")
    
    
    elif "sex" in command:
        if "your" in command or "you" in command:
            talk("I dont have a gender; I am an AI")
        else:
            talk("I'm not interested in that topic")    
        
    elif "Hi" in command or "hello" in command:
        user_name = get_user_name(command)
        if user_name:
            talk(f"Hello {user_name}, how are you?")
            print(f"Hello {user_name}, how are you?")
        else:
            talk("Hello! How can I help you?")
            print("Hello! How can I help you?")
    
    elif "thank you" in command:
        talk("You are always welcome")
        print("You are always welcome")
        
    # FORMAL COMMANDS   
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(current_time)
        talk("The current time is " + current_time)
        
    elif "open notepad" in command: 
        talk("Opening Notepad")
        subprocess.Popen(["notepad.exe"])
        
    elif "open calculator" in command:
        talk("Opening Calculator")
        subprocess.Popen(["calc.exe"])
        
    elif "play" in command:
        song = command.replace("play", "").strip()
        talk("Playing " + song) 
        pywhatkit.playonyt(song)
    
    elif any(keyword in command for keyword in ["who", "when","how", "what", "which"]):
        person = command.replace("who is", "").strip()
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    
    elif "joke" in command:
        talk(pyjokes.get_joke())
    
    elif "bye" in command:
        exit()
    else:
        sorry_response = random.choice(sorry_responses)
        talk(sorry_response)

run_eva()
