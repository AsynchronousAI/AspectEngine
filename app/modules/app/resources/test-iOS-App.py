import os # import the os module
projectName = "" # Change to the name of your project
platformName = "" # Change to the name of your platform

def emulate():
    # Emulate
    os.system("cd "+projectName) # change directory to the project folder
    os.system("cordova run "+platformName) # run the cordova emulate command

emulate()