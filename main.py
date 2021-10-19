# import psutil, os, signal

# while True:
#     a = int(input("Enter your task number: "))

#     if a == 1:
#         os.startfile(r"D:\d data\New songs\Makhna.mp3")

#     elif a == 2:
#         sig = signal.SIGTERM
#         for pid in (process.pid for process in psutil.process_iter() if process.name()=="Music.UI.exe"):
#             os.kill(pid, sig)

#     elif a == 3:
#         os.startfile(r"C:\Users\star\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code")
    
#     else:
#         break

import pyttsx3
