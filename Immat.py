import sqlite3
import time
from playsound import playsound
from scripts_other import Automation_Commands
import os
import pyautogui
from scripts_other.art import art
from pathlib import Path
import getpass

username = getpass.getuser()

# Getting current Path

final_Path = os.path.abspath(__file__)
final_Path = final_Path.replace('Immat.py','')

# Getting credentials

try:
    os.mkdir(Path.home() / 'IMMAT_Credentials')
    cred_path = (Path.home() / 'IMMAT_Credentials')
    checkFile = open(f'{cred_path}/credentials.txt', 'w')
    checkFile.write("Running For First Time")
    checkFile.close()
except:
    cred_path = (Path.home() / 'IMMAT_Credentials')

# Check if Running For First Time

phone = ""
password = ""
print(final_Path)
checkFile = open(f'{cred_path}/credentials.txt','r+')
contents = checkFile.read()

if contents == "Running For First Time":
    print(art)
    print("\nWelcome to IMMAT!\nNow use your iPhone to control your Mac using iMessage.")
    input("\nPress Enter to continue...")
    os.system('clear')
    password = input("Enter the password\nIt should not be equal to the Commands :-\n")
    os.system('clear')
    phone = input("Enter the iPhone number or E-mail :-\n")
    os.system('clear')
    checkFile.write("\n" + password + "\n")
    checkFile.write(phone + "\n")

else:
    print(art)
    with open(f'{cred_path}/credentials.txt','r+') as f:
        credentials = f.read().splitlines()
    password = credentials[1]
    phone = credentials[2]

checkFile.close()

print("\n****** Running ******\n")
print("\niMessage your Mac with 'yourPassword <Space> Help' to get the available commands\n")
print("\niMessage your Mac with 'yourPassword <Space> Exit' to Exit the program\n")

# Checks the latest Message for Command

def check_message(msg, row):

    if msg == "b0":
        Automation_Commands.turn_off_bluetooth()
        Automation_Commands.revertState(cur, conn, row)

    elif msg == "b1":
        Automation_Commands.turn_on_bluetooth()
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'help':
        Automation_Commands.helpCommand(phone, final_Path)
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'fmm':
        Automation_Commands.changeVolume(9)
        playsound(f"{final_Path}resources/FindMy.m4a")
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'sleepm':
        Automation_Commands.sleepMyMac()
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'wifi0':
        Automation_Commands.turn_off_Wifi()
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'music1':
        Automation_Commands.playMusic(final_Path)
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'music0':
        Automation_Commands.pauseMusic(final_Path)
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'prevsong':
        Automation_Commands.prevSong()
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'nextsong':
        Automation_Commands.nextSong()
        Automation_Commands.revertState(cur, conn, row)

    elif "changebrightness" in msg:
        value = msg.split('~',1)[1]
        Automation_Commands.changeBrightness(value)
        Automation_Commands.revertState(cur, conn, row)

    elif "changevolume" in msg:
        value = msg.split('~',1)[1]
        Automation_Commands.changeVolume(value)
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'ts':
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(fr'{final_Path}my_screenshot.png')
        Automation_Commands.takeScreenshot(final_Path, phone)
        Automation_Commands.revertState(cur, conn, row)

    elif "openapp" in msg:
        value = msg.split('~',1)[1]
        Automation_Commands.openApplication(value)
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'getbattery':
        Automation_Commands.getBattery(final_Path, phone)
        Automation_Commands.revertState(cur, conn, row)

    elif "openweb" in msg:
        value = msg.split('~',1)[1]
        Automation_Commands.openWebsites(value)
        Automation_Commands.revertState(cur, conn, row)

    elif "quitapp" in msg:
        value = msg.split('~',1)[1]
        Automation_Commands.quitApplication(value)
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'display0':
        Automation_Commands.displayOff()
        Automation_Commands.revertState(cur, conn, row)

    elif msg == 'display1':
        Automation_Commands.displayOn()
        Automation_Commands.revertState(cur, conn, row)

    elif "sleepafter" in msg:
        value = msg.split('~',1)[1]
        Automation_Commands.sleepSchedule(value, final_Path)
        Automation_Commands.revertState(cur, conn, row)

    elif "exit" in msg:
        Automation_Commands.revertState(cur, conn, row)
        exit()

    else:
        print("Command Not Found")
        Automation_Commands.revertState(cur, conn, row)

    time.sleep(1)

# Loops Infinity to get latest Message

while True:

    time.sleep(1)

    #-------- initialising chat.db ---------
    try:
        conn = sqlite3.connect(fr'/Users/{username}/Library/Messages/chat.db')
    except sqlite3.OperationalError:
        print("\n--Permission denied--\n\nTerminal needs to have full disk access for IMMAT to work.\n\nTo give full disk access to terminal :-\n\n1) Go to System Preferences\n\n2)Go to Security and privacy\n\n3) Click on Privacy Tab\n\n4) Scroll down to 'Full Disk Access\n\n5) Click on the Lock below\n\n6) Enter the password\n\n7) If Terminal is present on the right side then enable the full disk acces by clicking the checkmark\n\n8) Else click on plus (+) and add Terminal to the list'")
        print("\n\nReRun IMMAT after performing the steps\n")
        break

    cur = conn.cursor()

    # -------- Getting Messages ---------

    cur.execute("SELECT text FROM message")
    messages = []

    for name in cur.fetchall():
        messages.append(name)

    # -------- Getting Rows ---------

    cur.execute("SELECT ROWID FROM message ORDER BY ROWID DESC LIMIT 1")

    # -------- Getting latest message and Respective Row --------

    latestMessage = str(messages[len(messages) - 1])
    latestRow = str(cur.fetchone())

    # -------- Checking for Secret keyword ---------
    password = password.lower()
    latestMessage = latestMessage.lower()
    if password in latestMessage:
        # -------- Formatting last Message and Row ---------
        latestMessage = latestMessage.replace(password,'')
        badChars = [',', "'", '(', ')', "#", ' ']
        for i in badChars:
            latestMessage = latestMessage.replace(i, '')
            latestRow = latestRow.replace(i, '')

        # -------- Checking the command ---------
        print(latestMessage)
        check_message(latestMessage, latestRow)



