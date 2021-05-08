# IMMAT (iMessage Mac Automation Tool)

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub contributors](https://img.shields.io/github/contributors/ParthJadhav/IMMAT)
![GitHub stars](https://img.shields.io/github/stars/ParthJadhav/IMMAT)
![GitHub repo issues](https://img.shields.io/github/issues/ParthJadhav/IMMAT?label=issues)

IMMAT is a tool developed to control the MacOS operating system using iMessage on your iPhone.

IMMAT is created using Python and AppleScript.

## 🔖 Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed Python3 and have it working.
* You have a MacOS machine. With iMessage working.
* You have iPhone with iMessage working.
* Installed the dependencies from requirements.txt.

## 📦 Installing IMMAT

To install IMMAT, follow these steps:

Installing requirements :-
```
cd IMMAT

pip3 install -r requirements.txt
```

Running IMMAT (Foreground) :

❗️It is mandatory that you run it in foreground at first run.❗
```
cd IMMAT

python3 main.py
```

Running IMMAT (Background) :-
```
cd IMMAT

chmod +x main.py

nohup /path/to/main.py &

#*#*#*#*#*#*#*#*#*#*#*#*#

To stop :-

pkill -f main.py
```

## 🦋 Usage

IMMAT will only be running on Mac the commands would be given from iMessage on other devices.

Example - 

Password - ###\
Command - ts (Take Screenshot)

Message the below command through iMessage to Mac.
```
### Ts
```

This will reply you with the screenshot of the Mac.

These are the available commands :-

<img width="467" alt="Help" src="https://user-images.githubusercontent.com/42001064/117529945-33c17a00-aff8-11eb-8530-57f49f346265.png">

## 📱 Contact

If you want to contact me you can reach me at Jadhavparth99@gmail.com

## 📄 License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses MIT License.
