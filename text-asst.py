#This python will open apps from command line. It works on only two libraries - text to speech 'pyttsx3' and 'os'.

import pyttsx3
import os


print("Hello, I am chatbot program. I can open some apps for you, just text me your requirement.")
pyttsx3.speak("Hello, I am chatbot program. I will open some apps for you, chat with me.")
print("")

while True:
	print("What can I do for you? :", end="")
	pyttsx3.speak("What can I do for you?")
	p = input()

	if (("run" in p) or ("open" in p) or ("start" in p)) and ("chrome" in p) or ("browser" in p) :
	  pyttsx3.speak("Opening chrome")
	  os.system("chrome")
    
	elif (("run" in p) or ("open" in p) or ("start" in p)) and ("firefox" in p) or ("mozilla firefox" in p) :
	  pyttsx3.speak("Opening firefox browser")
	  os.system("firefox")

	elif (("run" in p) or ("open" in p) or ("start" in p)) and  (("notepad" in p) or ("editor" in p) or ("text editor" in p)) :
	  pyttsx3.speak("Opening notepad")
	  os.system("notepad")

	elif (("run" in p) or ("open" in p) or ("start" in p)) and  (("notepad++" in p) or ("notepad plus plus" in p)) :
	  pyttsx3.speak("Opening notepad plus plus")
	  os.system("notepad++")
    
	elif (("run" in p) or ("open" in p) or ("start" in p)) and  (("sublime text editor" in p) or ("sublime text" in p) or ("sublime" in p)) :
	  pyttsx3.speak("Opening sublime text editor")
	  os.system("subl")

	elif (("run" in p) or ("open" in p) or ("start" in p)) and  (("vs code" in p) or ("visual studio code" in p) or ("vscode" in p)) :
	  pyttsx3.speak("Opening vs code")
	  os.system("code")
	
	elif (("run" in p) or ("open" in p) or ("start" in p)) and  (("ms word" in p) or ("micosoft office word" in p) or ("word" in p)) :
	  pyttsx3.speak("Opening ms word")
	  os.system("WINWORD")

	elif (("run" in p) or ("open" in p) or ("start" in p)) and  (("ms powerpoint" in p) or ("micosoft office powerpoint" in p) or ("powerpoint" in p)) :
	  pyttsx3.speak("Opening ms powerpoint")
	  os.system("POWERPNT")

	elif (("run" in p) or ("open" in p) or ("start" in p)) and  (("ms excel" in p) or ("micosoft office excel" in p) or ("excel" in p)) :
	  pyttsx3.speak("Opening ms excel")
	  os.system("EXCEL")
    
	elif (("run" in p) or ("open" in p) or ("start" in p))  and (("player" in p) or ("media player" in p) or ("music player" in p)):
	  pyttsx3.speak("Opening windows media player")
	  os.system("wmplayer")

	elif (("run" in p) or ("open" in p) or ("start" in p))  and (("vlc" in p) or ("vlc player" in p)):
	  pyttsx3.speak("Opening vlc player")
	  os.system("vlc")

	elif("hi"in p) or ("hello"in p) or ("hey"in p):
	  pyttsx3.speak("Hello! Please tell me which application you want to open.")

	elif  ("exit" in p)  or ("quit" in p) or ("close" in p):
	  pyttsx3.speak("Thank youf for using me. Have a nice day, Bye!")
	  break

	else:
	  pyttsx3.speak("Sorry, I can't understand this, please try again!")
	

