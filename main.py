import datetime, psutil, os, signal
import speech_recognition as sr
import random
from playsound import playsound
import requests, json

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

        elif command == "i want to play game" or command == "can you play me a game" or command == "game" or command == "i want to play a game" or command == "play me a game":
            speak("Ok sir")
            cpoints = 0
            upoints = 0
            print("Welcome to my game , read instructions carefully and enjoy the game :))")
            print("Choose from the following each time.. \nS:- For Snake\nW:- For Water\nG:- For Gun")
            print("Remember to write your choise in Capital each time otherwise your choice will not be taken by the computer")
            for i in range(10):
                objects = ["Snake", "Water", "Gun"]
                computer = random.choice(objects)
                user = input("Now enter your choice: ")
                
                if user == "S" and computer == "Snake":
                    print("Same choice", "\t\t\t\t\t\tYou=", upoints, ",Computer=", cpoints)
                    playsound('D:\\game sounds\\same choice1.mp3')
                    
                elif user == "S" and computer == "Water":
                    upoints+=1
                    print("Results\nYou-Snake", "Computer-", computer,"\t\t\t\tYou=",upoints,",Computer=",cpoints)
                    playsound('D:\\game sounds\\u get point.mp3')
                    
                elif user == "S" and computer == "Gun":
                    cpoints += 1
                    print("Results\nYou-Snake", "Computer-", computer, "\t\t\t\tYou=",upoints,",Computer=",cpoints)
                    playsound('D:\\game sounds\\C get point.mp3')
                    
                elif user == "W" and computer == "Snake":
                    cpoints += 1
                    print("Results\nYou-Water", "Computer-", computer, "\t\t\t\tYou=", upoints, ",Computer=", cpoints)
                    playsound('D:\\game sounds\\C get point.mp3')
                    
                elif user == "W" and computer == "Water":
                    print("Same choice", "\t\t\t\t\t\tYou=", upoints, ",Computer=", cpoints)
                    playsound('D:\\game sounds\\same choice1.mp3')
                    
                elif user == "W" and computer == "Gun":
                    upoints+=1
                    print("Results\nYou-Water", "Computer-", computer, "\t\t\t\tYou=", upoints, ",Computer=", cpoints)
                    playsound('D:\\game sounds\\u get point.mp3')
                    
                elif user == "G" and computer == "Snake":
                    upoints+=1
                    print("Results\nYou-Gun", "Computer-", computer, "\t\t\t\tYou=", upoints, ",Computer=", cpoints)
                    playsound('D:\\game sounds\\u get point.mp3')
                    
                elif user == "G" and computer == "Water":
                    cpoints+=1
                    print("Results\nYou-Gun", "Computer-", computer, "\t\t\t\tYou=", upoints, ",Computer=", cpoints)
                    playsound('D:\\game sounds\\C get point.mp3')
                    
                elif user == "G" and computer == "Gun":
                    print("Same choice", "\t\t\t\t\t\tYou=", upoints, ",Computer=", cpoints)
                    playsound('D:\\game sounds\\same choice1.mp3')
                    
                else:
                    print("Invalid input !!! Enter S or W or G")
                    
            print("Final Results","You=", upoints, ",Computer=", cpoints)
            if upoints<cpoints:
                print("Computer Wins !!! Better luck next time")
                playsound('D:\\game sounds\\You lose sound.mp3')
            elif upoints>cpoints:
                print("You Won the match!!! Congratulations !!!")
                playsound('D:\\game sounds\\Kids Cheering.mp3')
            else:
                print("Match draw !! Your played very well...")
                playsound('D:\\game sounds\\match draw.mp3aw.mp3')

        elif command == "tell me some news" or command == "tell me some news headlines" or command == "news":
            speak("Ok Sir...")
            speak("Which type of news you want to listen?")
            a = input("1: General\n2: Hacker News\n3: Technology\n4: sports\n5: entertainment\n6: Business\n7: Science\n8: Health\n")
            if a == '1':
                news_channel = "the-times-of-india"
            elif a == '2':
                news_channel = "Hacker-News"
            elif a == '3':
                news_channel = "Ars-Technica"
            elif a == '4':
                news_channel = "NHL-News"
            elif a == '5':
                news_channel = "Entertainment-Weekly"
            elif a == '6':
                news_channel = "The-Wall-Street-Journal"
            elif a == '7':
                news_channel = "National-Geographic"
            elif a == '8':
                news_channel = "Medical-News-Today"
            else:
                print("Invalid news topic number entered.. Starting telling general news..")
                speak("Invalid news topic number entered.. Starting telling general news")
                news_channel = "the-times-of-india"
            try:
                url = f"https://newsapi.org/v2/top-headlines?sources={news_channel}&apiKey=31c98e95bba3475f90f5cd5ec2f0fceb"
                news = requests.get(url).text
                news_dict = json.loads(news)
                # print(news_dict['articles'])
                arts = news_dict['articles']
                speak("Speaking news.. Listen carefully....")
                for articles in arts:
                    print(f"{articles['title']}\nMore-{articles['url']}\n")
                    speak(articles['title'])
                    speak("Moving on to the next news..")
                speak("Thanks for listening")
            except Exception as e:
                print(e)
            

        else:
            print("Sorry i can't help you in that...")
            speak("Sorry i can't help you in that...")



