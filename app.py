import datetime
import pyttsx3
import speech_recognition as sr
import os
import cv2 

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user commands
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        speak("Sorry, I didn't understand.")
        return None
    except sr.RequestError as e:
        print("Sorry, there was an error. Check your internet connection.")
        speak("Sorry, there was an error. Check your setup.")
        speak(str(e))
        return None

# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    return current_time

# Function to get details about the AI
def get_details():
    details = "I am an AI assistant programmed to tell time, set alarms, save notes, and perform basic tasks."
    print(details)
    return details

# Function to set an alarm
def set_alarm():
    speak("Please enter the alarm time in 24-hour format (HH:MM)")
    alarm_time = input("Alarm time (HH:MM): ")
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! It's time!")
            speak("Wake up! It's time!")
            break

# Function to save notes
def save_note():
    speak("Please speak the content of your note.")
    note_content = listen()
    with open("notes.txt", "a") as file:
        file.write(note_content + "\n")
    speak("Note saved successfully.")

# Function to read the saved notes
def read_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if len(notes) == 0:
                print("You have no saved notes.")
                speak("You have no saved notes.")
            else:
                speak("Here are your saved notes:")
                for note in notes:
                    print(note)
                    speak(note)
    except FileNotFoundError:
        speak("You have no saved notes.")

# Function to open the camera
def open_camera():
    cap = cv2.VideoCapture(0)  # 0 indicates the default camera, you can change it if you have multiple cameras

    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera Feed', frame)

        # Break the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main program loop
while True:
    speak("How can I assist you?")
    command = listen()

    # Check if the command contains the word "exit" or "quit"
    if "exit" in command or "quit" in command:
        speak("Goodbye!")
        break

    # Check if the command contains the word "ARIA"
    #if "aria" in command:
     #   speak("ARIA detected. How can I help?")
      #  continue  # Skip the rest of the loop and start listening again

    # Rest of the code for other functionalities based on different conditions
    if "time" in command:
        current_time = get_time()
        speak("The current time is " + current_time)

    elif "details" in command or "about you" in command:
        assistant_details = get_details()
        speak(assistant_details)

    elif "alarm" in command or "set alarm" in command:
        set_alarm()

    elif "save note" in command or "take note" in command:
        save_note()

    elif "read notes" in command or "view notes" in command:
        read_notes()

    elif "camera" in command or "open camera" in command:
        speak("Opening the camera. enter 'q' to close the camera.")
        print("Opening the camera. enter 'q' to close the camera.")

        open_camera()
