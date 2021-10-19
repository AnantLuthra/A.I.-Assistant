import datetime, psutil, os, signal
import speech_recognition as sr

# import pyttsx3
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print(voices)
# engine.setProperty('voice', voices[1].id)
# def speak(str):
#     engine.say(str)
#     engine.runAndWait()

def speak(str):
    '''
    Function for speaking of program.
    '''
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def wisher():
    '''
    This function wishes user as per time.
    '''

    final_time = int(datetime.datetime.now().hour)

    if final_time > 4 and final_time < 12:
        speak("Good Morning Sir..")

    elif final_time < 16 and final_time >= 12:
        speak("Good afternoon Sir..")

    elif final_time >= 16 and final_time < 19:
        speak("Good evening Sir..")

    elif final_time >= 18 and final_time < 24:
        speak("Good night Sir..")

    elif final_time < 4:
        speak("Sir it's very dark night what are you waiting for sleep now..")
    
    speak("I am Poker, Please tell me how may I help you....")

def listen():
    '''
    Take command from the user by its voice and return a string as output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.operation_timeout = 15
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == '__main__':
    wisher()

    while True:
        command = listen()
        command = command.lower()
        if command == "gana suna de achcha sa" or command == "play a song" or command == "play music":
            os.startfile(r"D:\d data\New songs\Makhna.mp3")

        elif command == "kya baja diya ye band kr ise" or command == "please close this" or command == "please stop this":
            sig = signal.SIGTERM
            for pid in (process.pid for process in psutil.process_iter() if process.name()=="Music.UI.exe"):
                os.kill(pid, sig)

        elif command == "open code" or command == "coding karne ka man kr rha hai":
            os.startfile(r"C:\Users\star\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code")

        elif command == "exit" or command == "close" or command == "quit" or command == "poker close" or command == "good bye poker" or command == "goodbye poker":
            print("Ok closing..")
            speak("Ok sir have a good day ...")
            break

        elif command == "who are you" or command == "kaun hai tu" or command == "poker who are you":
            print("I am Pokar, made by Anant, I can help you. Tell me what to do?")
            speak("I am Pokar, made by Anant, I can help you. Tell me what to do?")

        elif command == "open google":
            print("Opening...")
            speak("Opening...")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome")
        
        elif command == "i am feeling tired poker" or command == "feeling tired" or command == "feeling tired poker":
            speak("Should I play some music for you?")
            command = listen()
            if command == "ok" or command == "ok poker" or command == "yes":
                speak("Which type of music do want to play..")
                command = listen()
                if command == "anything" or command == "whatever you want":
                    os.startfile(r"D:\d data\New songs\SAKHIYAN.mp3")
                else:
                    pass
            else:
                speak("Ok sir...")
         
        elif command == "good job poker" or command == "thankyou poker" or command == "you helped me a lot poker" or command == "thanks":
            speak("It's my pleasure sir...")

        else:
            print("Sorry i can't help you in that...")
            speak("Sorry i can't help you in that...")



