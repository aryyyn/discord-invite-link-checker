import requests
import os
import webbrowser

clear = lambda: os.system('cls')
txt = "Join the"
myfile = open("discordinvitelinks.txt", "r")
myline = myfile.readline(100)
while myline:
    clear = lambda: os.system('cls')
    data = requests.get("https://discord.gg/" + myline).text
    if txt in data:
        print(myline + "correct")
    else:
        print("bad")
    myline = myfile.readline()


