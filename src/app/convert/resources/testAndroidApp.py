# Description: 
# This script emulates a Cordova project (for Android) that is located in a 
# folder on the computer. It checks if the project exists, and if it does, then 
# it emulates the project.

# Function names:
# checkProjectExists
# emulateProject

# Variable names:
# projectName
# projectFolder

# Context:
# The script is used in a Python script to emulate Cordova projects on Android.

# Download dependencies
import os
import sys
import argparse

# Create variables
projectName: str = sys.argv[1:][0] # Set the name of your project here
projectFolder: str = sys.argv[1:][1] # Set the path to the folder containing your projects

# Create functions
def checkProjectExists(projectName: str, projectFolder: str) -> bool:
    if not os.path.isdir(projectFolder + "/" + projectName):
        return False
    else:
        return True

def emulateProject(projectName: str, projectFolder: str):
    os.chdir(projectFolder + "/" + projectName)
    os.system("cordova run android")

# Check if the project exists
if not checkProjectExists(projectName, projectFolder):
    print("ERROR: Project does not exist! Aborting...")
    sys.exit(1)

# Emulate
emulateProject(projectName, projectFolder)