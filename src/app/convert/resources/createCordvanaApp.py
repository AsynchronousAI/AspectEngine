# Download dependencies
import os
import platform
import sys
from typing import List
operatingSystem: str = platform.system()

# Create variables
projectName: str = sys.argv[1:][0]
android: bool = sys.argv[1:][1]
iOS: bool = sys.argv[1:][2]
packageName: str = sys.argv[1:][3]
options: str = sys.argv[1:][4]
plugins: list = sys.argv[1:][5]

# Create cordova app
createCommand: str = "cordova create "+ projectName+ packageName+"."+projectName+ options
print("Creating cordova app...")
os.system(createCommand)
os.system("cd "+projectName)

# Add code
## not done yet

# Add platforms
if android:
    print("Adding android platform...")
    try:
        os.system("cordova platform add android")
    except:
        print("Android platform already added")
elif iOS:
    print("Adding ios platform...")
    try:
        os.system("cordova platform add ios")
    except:
        print("iOS platform already added")

# Install plugins
for i in plugins:
    print("Installing "+i+"...")
    try:
        os.system("cordova plugin add "+i)
    except:
        print("Plugin already installed")

# Build
if android:
    print("Building android app...")
    os.system("cordova build android")
elif iOS:
    print("Building ios app...")
    os.system("cordova build ios")