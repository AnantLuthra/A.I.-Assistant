import datetime, psutil, os, signal, requests, json, random, wikipedia, webbrowser, pyautogui, time
import speech_recognition as sr
from playsound import playsound

# Code for tuning voice of assistant into a famale voice...
# import pyttsx3
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# def speak(str):
#     engine.say(str)
#     engine.runAndWait()

with open("details.txt") as f:
    data = f.read()
    info = data.split("\n")

def speak(str):
    '''
    Function for speaking of program.
    '''
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def news_teller():
    speak("Which type of news you want to listen?")
    print("1: General\n2: Hacker News\n3: Technology\n4: sports\n5: entertainment\n6: Business\n7: Science\n8: Health\n")
    speak("General, Hacker News, Technology, sports, entertainment, Business, Science or health?")
    a = listen()
    a = a.lower()
    if a == 'general':
        news_channel = "the-times-of-india"
    elif a == 'hacker news':
        news_channel = "Hacker-News"
    elif a == 'technology':
        news_channel = "Ars-Technica"
    elif a == 'sports':
        news_channel = "NHL-News"
    elif a == 'entertainment':
        news_channel = "Entertainment-Weekly"
    elif a == 'business':
        news_channel = "The-Wall-Street-Journal"
    elif a == 'science':
        news_channel = "National-Geographic"
    elif a == 'health':
        news_channel = "Medical-News-Today"
    else:
        print("Invalid news topic number entered.. Starting telling general news..")
        speak("Invalid news topic number entered.. Starting telling general news")
        news_channel = "the-times-of-india"
    try:
        url = f"https://newsapi.org/v2/top-headlines?sources={news_channel}&apiKey={info[0]}"
        news = requests.get(url).text
        news_dict = json.loads(news)
        # print(news_dict['articles'])
        arts = news_dict['articles']
        speak("Speaking news.. Listen carefully....")
        a = len(arts)
        for index, articles in enumerate(arts):
            if index != a - 1:
                print(f"{articles['title']}\nMore-{articles['url']}\n")
                speak(articles['title'])
                speak("Moving on to the next news..")
            else:
                print(f"{articles['title']}\nMore-{articles['url']}\n")
                speak(articles['title'])
        speak("Thanks for listening")
    except Exception as e:
        print(e)

def snake_water_gun():
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
        playsound('D:\\game sounds\\match draw.mp3')

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
    
    speak("Please tell me how may I help you....")

def task_closer(app):
    try:
        sig = signal.SIGTERM
        for pid in (process.pid for process in psutil.process_iter() if process.name()==f"{app}.exe"):
            os.kill(pid, sig)
    except Exception as e:
        speak("Something went wrong!! Couldn't close the given app...")

def command_writer(word, sleep_time):
    for i in word:
        pyautogui.press(i)
    pyautogui.press('enter')
    time.sleep(sleep_time)

def after_reaching_directory():
    '''
    This function complete the task after reaching the main directory which is to be updated 
    as told by user...
    '''
    time.sleep(2)
    pyautogui.moveTo(x=955, y=527)
    pyautogui.click()
    pyautogui.rightClick()
    for i in range(9):
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(2)
    command_writer("git st", 1)
    command_writer("git add .", 2)
    speak("Do you wanna add custom message for committing file?")
    opinion = listen().lower()
    if "yes" in opinion:
        speak("So tell your custom message...")
        a = listen().lower()
    else:
        update_list_name = ["Added new feature", "Updated main.py"]
        a = random.choice(update_list_name)
    
    command_writer(f"git commit -m \"{a}\"", 2)
    command_writer("git push origin master", 9)
    command_writer("exit", 1)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'tab')
    speak("Updated git..")
    return "Done\n"

def name_searcher(directory):
    '''
    This function takes directory name and enter in the directory
    and runs after process...
    '''
    for i in directory:
        pyautogui.press(i)
    pyautogui.press("enter")
    after_reaching_directory()

def url_open_google(url):
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

def listen():
    '''
    Take command from the user by its voice and return a string as output.
    '''
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.operation_timeout = 15
            audio = r.listen(source)
        
    except OSError:
        speak("Your microphone is not plugged in..")
    
    except Exception as e:
        pass

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except sr.RequestError:
        speak("Please check your internet connection..")
        

    except Exception as e:
        print(e)
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned.
    
    return query
    
def time_sleep(time2, time_format):
    if time_format == "seconds":
        speak(f"Ok sir sleeping for {time2} seconds...")
        time.sleep(int(time2))
    
    elif time_format == "minutes":
        speak(f"Ok sir sleeping for {time2} minutes...")
        a = int(time2) * 60
        time.sleep(a)


if __name__ == '__main__':
    wisher()

    while True:
        
        command = listen().lower()

        try:
            if 'play music' in command:
                speak("Ok playing...")
                music_folder = "D:\\d data\\New songs"
                songs = os.listdir(music_folder)
                a = random.randint(1, len(songs) - 1)
                os.startfile(os.path.join(music_folder, songs[a]))

            elif command == "kya baja diya ye band kr ise" or command == "stop music" or command == "close music":
                speak("Ok closing..")
                task_closer("Music.UI")

            elif command == "close chrome" or command == "exit chrome" or command == "close google chrome" or command == "google band kar de":
                speak("Ok closing...")
                task_closer("chrome")

            elif 'open code' in command:
                speak("Opening...")
                os.startfile(r"C:\Users\star\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code")

            elif 'quit' in command:
                print("Ok closing..")
                speak("Ok sir have a good day ...")
                break

            elif 'who are you' in command:
                print("I am A.I. developed by Anant, I can help you. Tell me what to do?")
                speak("I am A.I. developed by Anant, I can help you. Tell me what to do?")

            elif 'open google' in command:
                print("Opening...")
                speak("Opening...")
                os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome")

            elif 'feeling tired' in command:
                speak("Should I play some music for you?")
                command = listen()
                if command == "ok" or command == "ok poker" or command == "yes":
                    speak("Which type of music do want to play.. binaural beats or lyrics one??")
                    command = listen().lower()
                    if "binaural beats" in command:
                        speak("Ok playing...")
                        music_folder = "D:\\d data\\NCS music"
                        songs = os.listdir(music_folder)
                        a = random.randint(1, len(songs) - 1)
                        os.startfile(os.path.join(music_folder, songs[a]))
                    elif "lyrics one" in command:
                        speak("Ok playing...")
                        music_folder = "D:\\d data\\New songs"
                        songs = os.listdir(music_folder)
                        a = random.randint(1, len(songs) - 1)
                        os.startfile(os.path.join(music_folder, songs[a]))

                    else:
                        speak("Ok sir...")

            elif "good job" in command:
                speak("It's my pleasure sir...")

            elif command == "i want to play game" or command == "can you play me a game" or command == "game" or command == "i want to play a game" or command == "play me a game":
                speak("Ok sir")
                snake_water_gun()

            elif 'news' in command:
                speak("Ok Sir...")
                news_teller()

            elif command == "hii" or command == "hi" or command == "hello" or command == "namaste":
                if command == "namaste":
                    speak("Namaste.. Tell me how can i help you...")
                else:
                    speak("Hello sir i am poker tell me how may i help you...")

            elif 'wikipedia' in command:
                try:
                    speak("Searching Wikipedia....")
                    command = command.replace("wikepedia", "")
                    results = wikipedia.summary(command, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                except wikipedia.exceptions.PageError:
                    speak("Could not find about the given data..")

                except Exception as e:
                    print("Something went wrong..")

            elif 'open youtube' in command:
                url_open_google("youtube.com")

            elif 'the time' in command:
                a = datetime.datetime.now().strftime("%H:%M:%S")
                list1 = a.split(":")
                speak(f"Sir the time is{list1[0]} hours {list1[1]} minutes and {list1[2]} seconds.")

            elif 'switch window' in command:
                pyautogui.hotkey('alt', 'tab')

            elif 'click on start' in command:
                pyautogui.press('win')

            elif 'open settings' in command:
                pyautogui.press('win')
                time.sleep(1)
                pyautogui.moveTo(x=23, y=655)
                pyautogui.click()

            elif 'startup folder' in command:
                pyautogui.hotkey('win', 'r')
                time.sleep((.5))
                textt = "shell:startup"
                for i in textt:
                    pyautogui.press(i)
                pyautogui.press('enter')

            elif command == 'update directory on github':
                speak("Ok sir getting up to date...")
                pyautogui.hotkey('win', 'd')
                os.startfile(r"D:\Python projects")
                time.sleep(1)
                pyautogui.press('f11')
                speak("Which directory you want to update on github?")
                directory = listen().lower()
                name_searcher(directory)
                continue
            
            elif "your name" in command:
                speak("My name is not defined but you can call me with any name..")

            elif "typeracer" in command:
                speak("Opening")
                url_open_google("10ff.net")

            elif "open typing master" in command:
                speak("Opening")
                os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\TypingMaster\Typing Master")

            elif command == "close typing master":
                speak("Ok closing")
                task_closer("tmaster")
            
            elif "instagram" in command:
                speak("Opening..")
                url_open_google("instagram.com")

            elif "python playlist" in command:
                speak("Opening..")
                url_open_google("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")

            elif "sleep for" in command:
                time_and_measure = command.split(" ")
                time2 = ""
                time_format = ""
                for i in time_and_measure:
                    if time2 and time_format != "":
                        break
                    if i.isnumeric():
                        time2 = int(i)
                    if i == "seconds" or i == "minutes":
                        time_format = i
                
                time_sleep(time2, time_format)
                speak("Waked up sir...Tell me what to do now...")

            elif "are you there" in command:
                speak("Yes sir I am always their for you")

            elif "wish me" in command:
                speak("Best wishes for you sir...")

            elif "tekken 3" in command:
                speak("Opening")
                os.startfile(r"D:\d data\takken 3\Tekken_3")

            elif "scroll down" in command:
                speak("Ok sir...")
                time.sleep(2)
                pyautogui.scroll(-50)
                while True:
                    speak("Do you want to scroll down more???")
                    more1 = listen().lower()
                    if "yes" in more1:
                        amount = more1.split(" ")
                        for i in more1:
                            if i == "little":
                                pyautogui.scroll(-200)
                                break
                            if i == "jyada":
                                pyautogui.scroll(-300)
                                break
                            if i == "bahut":
                                pyautogui.scroll(-400)
                                break
                            else:
                                pyautogui.scroll(-200)
                                break

                    else:
                        speak("Ok sir..")
                        break
            
            elif command == "minimise all windows":
                speak("Ok sir..")
                pyautogui.hotkey('win', 'd')

            else:
                print("Sorry i can't help you in that...\n")

        except Exception as e:
            speak("Something went wrong..")