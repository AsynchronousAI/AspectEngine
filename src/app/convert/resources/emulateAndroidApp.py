# This code emulates a cordova project
# The code takes the name of the project folder as input and runs the command
# 'cordova emulate android' in that folder. The code will stop and display an error
# message if the command fails.
# The function used is os.system()
# The variable used is projectName
# The purpose of this code is to emulate a cordova project in Android Studio

# Download dependencies
import os
import sys

# Create variables
projectName: str = sys.argv[1:][0] # this is the name of the folder that contains the project

# Emulate
os.system("cd "+projectName)
os.chdir(projectName)
print("Emulating project: "+projectName)
try:
    os.system("cordova emulate android")
except:
    sys.exit("Error: Failed to emulate project")