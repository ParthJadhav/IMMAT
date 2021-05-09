#!/usr/bin/env python3
import sqlite3
import time
from playsound import playsound
from scripts import Automation_Commands
import os
import pyautogui
from scripts.art import art
from pathlib import Path
import getpass

username = getpass.getuser()

# Getting current Path

final_Path = os.path.abspath(__file__)
final_Path = final_Path.replace('main.py','')

# Check if Running For First Time

phone = ""
password = ""
print(final_Path)
checkFile = open(f"{final_Path}resources/credentials.txt", 'r+')
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
    print("Running")

else:
    print(art)
    with open(f"{final_Path}resources/credentials.txt") as f:
        credentials = f.read().splitlines()
    password = credentials[1]
    phone = credentials[2]
    print("\n****** Running ******")

checkFile.close()

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
        playsound('/Users/parthjadhav/IMMAT/resources/FindMy.m4a')
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
        #im2 = pyautogui.screenshot('my_screenshot.png')
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

    else:
        print("Command Not Found")
        Automation_Commands.revertState(cur, conn, row)

    time.sleep(1)

# Loops Infinity to get latest Message

while 1 < 2:

    #-------- initialising chat.db ---------

    conn = sqlite3.connect(fr'/Users/{username}/Library/Messages/chat.db')
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



