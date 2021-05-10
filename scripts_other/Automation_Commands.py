import os
import applescript
import psutil
import time

def helpCommand(iPhoneNumber,path):
    filePath = path + "resources/"
    os.system(f"osascript {path}appleScripts/help.applescript {filePath} {iPhoneNumber}")

def revertState(cursor, db, row):
    sql = f"UPDATE message SET text = 'Command Replaced' WHERE ROWID = '{row}'"
    cursor.execute(sql)
    db.commit()

def turn_on_bluetooth():
    os.system("blueutil -p 1")

def turn_off_bluetooth():
    os.system("blueutil -p 0")

def turn_off_Wifi():
    os.system("networksetup -setairportpower airport off")

def sleepMyMac():
    os.system("pmset sleepnow")

def playMusic(path):
    applescript.run(f"{path}appleScripts/playMusicScript.applescript")

def pauseMusic(path):
    applescript.run(f"{path}appleScripts/pauseMusicScript.applescript")

def changeBrightness(value):
    value = float(value)/10
    os.system(f"/usr/local/bin/brightness {value}")

def changeVolume(value):
    os.system(f"osascript -e 'set Volume {value}'")

def takeScreenshot(path,phone):
    os.system(f"osascript {path}appleScripts/takeScreenshot.applescript {path} {phone}")

def takePicture(iPhoneNumber,path):
    os.system(f"osascript {path}appleScripts/takePicture.applescript {iPhoneNumber}")

def openApplication(app):
        #os.system(f"open /System/Applications/'{app}'.app")
        if os.system(f"open /Applications/'{app}'.app") == 0:
            os.system(f"open /Applications/'{app}'.app")
        else:
            os.system(f"open /System/Applications/'{app}'.app")

def getBattery(path,phone):
    batteryPercent = str(psutil.sensors_battery().percent)
    batteryPercent = batteryPercent + "%"
    os.system(f"osascript {path}appleScripts/getBattery.applescript {phone} {batteryPercent}")

def openWebsites(website):
    cmd = f"""osascript -e '
        tell application "Safari"
	open location "{website}"
	activate
end tell
'"""
    os.system(cmd)

def prevSong():
    cmd = f"""osascript -e '
            tell application "Music" to play (previous track)
    '"""
    os.system(cmd)

def nextSong():
    cmd = f"""osascript -e '
            tell application "Music" to play (next track)
    '"""
    os.system(cmd)

def quitApplication(app):
    app.capitalize()
    cmd = f"""osascript -e '
                tell application "{app}" to quit
        '"""
    os.system(cmd)

def displayOff():
    cmd = "/usr/local/bin/brightness 0"
    os.system(cmd)

def displayOn():
    cmd = "/usr/local/bin/brightness 0.8"
    os.system(cmd)

def sleepSchedule(inTime,path):
    time.sleep(int(inTime))
    applescript.run(f"{path}appleScripts/delaySleep.applescript")