#import various modules required

import os
import pyttsx3 
import time
import webbrowser
from datetime import date,datetime

ron = pyttsx3.init()

# changing default male voice to female voice

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
ron.setProperty('voice', voice_id) 
ron.setProperty('rate', 165)
ron.setProperty('volume', 0.7) 

help_list = ['\"Open\close notepad\"','\"Open\close firefox\"','\"Open\close Windows Media Player\"','\"Open gaana\"','\"Open youtube\"','\"www.google.com\"','\"Play me a song\"','\"what day is it today\"',]
print("-> Hi, how can i help you ")
ron.say("hi, how can i help you ")
ron.runAndWait()

print("-> There's a lot I can help you with")
ron.say("There's a lot I can help you with")
ron.runAndWait() 

print("-> You can try writing ")
ron.say("You can try writing")
ron.runAndWait() 

   # starter commands

print()
print("  \"Open firefox\"")
print("  \"What is the time\"")
print("  \"Play me a song\"")
print("  \"Open Whatsapp\"")
print("  \"Help\"")
print()


a = 1
i = 1
fail = 0
while a == 1:
  print(end="					-> ")
  reply_raw = input()
  reply_2 = reply_raw.lower()

  # help section

  if "help" in reply_2:
    print(" Some of the commands that can be used are")
    ron.say("Some of the commands that can be used are listed below")
    ron.runAndWait()
    for h in help_list1:
      print(h)
    print()
    print("-> If you want to open a\n   certain program you may first give a command\n   \" Open a program\"\n   and then enter the program name\n   to open the program.\n")
    print("-> You can also open certain web pages\n   for applications such as whatsapp.")
    print(end="   ")
    for j in range(0,10):
      print(".",end=" ")
      time.sleep(1)
    print()
  if ("run" in reply_2) or ("open" in reply_2) or ("play" in reply_2) or ("execute" in reply_2) or ("what" in reply_2) or ("tell" in reply_2):
    if "firefox" in reply_2:
      ron.say("Opening firefox")
      ron.runAndWait() 
      os.system("firefox")

    elif ("notepad" in reply_2) or ("editor" in reply_2):
      ron.say("Opening notepad")
      ron.runAndWait() 
      os.system("notepad")

    elif ("media" in reply_2) or ("player" in reply_2):
      ron.say("Opening Windows Media Player")
      ron.runAndWait() 
      os.system("wmplayer")

    elif ("song" in reply_2):
      ron.say("Sure, asking gaana to play some music for you")
      ron.runAndWait() 
      webbrowser.open('https://gaana.com/song/blood-water', new=2)

    elif ("date" in reply_2):
      ron.say("Today is ")
      ron.runAndWait() 
      today = date.today()
      print("->> Today is ",today)
      ron.say(today)

    elif ("time" in reply_2):
      ron.say("time is")
      ttime = datetime.now()
      now_time = ttime.strftime("%H:%M:%S")
      print("->> Time is ",now_time)
      ron.say(now_time)
      ron.runAndWait()

    elif ("day" in reply_2):
      ron.say("day today is")
      ron.runAndWait()
      tday =datetime.now()
      print("->> Day today is ",tday.strftime("%A"))
      ron.say(tday.strftime("%A"))

    elif ("program" in reply_2) or ("application" in reply_2) or ("executable" in reply_2):
      ron.say("-> enter the program name to open the program")
      ron.runAndWait() 
      print(end="					-> ")
      reply_3 = input()
      ron.say("Opening")
      ron.say(reply_3)
      ron.runAndWait() 
      os.system(reply_3)

    elif ("whatsapp" in reply_2) or ("editor" in reply_2):
      ron.say("Sure, just wait a second ")
      ron.runAndWait() 
      webbrowser.open('https://web.whatsapp.com', new=2)

    elif "close" not in reply_2:
      print("-> Sorry, i did not understand\n   your command")
      ron.say("Sorry")
      ron.say("i did not understand your command")
      ron.runAndWait()
      fail += 1

  elif ("www" in reply_2) or ("https" in reply_2) or ("http" in reply_2) or (".com" in reply_2):
    ron.say("opening Web page")
    ron.runAndWait()
    webbrowser.open(reply_2, new=2)

  elif ("exit" in reply_2) or ("stop" in reply_2):
      print("-> Goodbye, nice talking to you")
      ron.say("Goodbye, nice talking to you")
      ron.runAndWait()
      break

  elif ("close" not in reply_2) and ("help" not in reply_2):
    print("Sorry, i did not understand\n   your command")
    ron.say("Sorry")
    ron.say("i did not understand your command")
    ron.runAndWait()
    fail += 1

  # for closing applications

  if ("close" in reply_2):
    if "firefox" in reply_2:
      ron.say("closing firefox")
      ron.runAndWait() 
      os.system("TASKKILL /F /IM firefox.exe")

    elif ("notepad" in reply_2):
      ron.say("closing notepad")
      ron.runAndWait() 
      os.system("TASKKILL /F /IM notepad.exe")

    elif ("media" in reply_2) or ("player" in reply_2):
      ron.say("closing Windows Media Player")
      ron.runAndWait() 
      os.system("TASKKILL /F /IM wmplayer.exe")

    elif "help" not in reply_2:
      print("Sorry, i did not understand\n   your command")
      ron.say("Sorry")
      ron.say("i did not understand your command")
      ron.runAndWait()
      fail += 1

  # how to stop the program

  if i <=1:
    print("-> Just so you know, you can\n   stop this chat anytime by\n   just saying me to stop")
    ron.say("Just so you know")
    ron.say("you can stop this chat anytime by just saying me to stop")
    ron.runAndWait() 
    print("-> But, did i also tell you\n   that i absolutely love\n   chating with you") 
    ron.say("But, did i also tell you")
    ron.say("that i absolutely love chating with you")
    ron.runAndWait()

  #if user fails to interact properly

  if fail == 2:
    print("-> looks like you are having trouble\n   interacting with me")
    ron.say("looks like you are having trouble interacting with me")
    print("-> You can always ask for my help \n   if you are having trouble interacting with me")
    ron.say("You can always ask for my help if you are having trouble interacting with me")
    ron.runAndWait()
  print("-> Do you want me to do anything else ?")
  ron.say("Do you want me to do anything else")
  ron.runAndWait()
  i = i+1
