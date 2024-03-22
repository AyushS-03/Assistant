import speech_recognition as sr
import pyttsx3
import os

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to execute commands
def execute_command(command):
    if "open notepad" in command:
        os.system("notepad.exe")
        speak("Opening Notepad")
    elif "open calculator" in command:  
        os.system("calc")
        speak("Opening Calculator")
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
        speak("Shutting Down")

# Main function to listen for voice commands
def main():
    speak("Hello! I am JARVIS and I'm your digital assistant. How can I assist you today?")
    
    try:
        while True:
            with sr.Microphone() as source:
                print("Adjusting for ambient noise...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                try:
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                except sr.WaitTimeoutError:
                    print("No speech detected")
                    continue

            if audio is not None:  # Check if audio is captured
                print("Recognizing...")
                try:
                    command = recognizer.recognize_google(audio).lower()
                    print("Command:", command)

                    if "hey there" in command:
                        speak("Yes, how can I help you?")
                    else:
                        execute_command(command)
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand that.")
                except sr.RequestError as e:
                    print("Error: Could not request results; {0}".format(e)) 
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Program terminated by user.")

if __name__ == "__main__":
    main()
