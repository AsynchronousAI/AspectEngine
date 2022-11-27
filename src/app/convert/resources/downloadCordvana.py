import os
import platform
from typing import List
# Get the operating system name, e.g. 'Windows', 'Linux', 'Darwin' (macOS), etc.
operatingSystem: str = platform.system()

# Install Cordova on Windows, or on Linux or macOS if the user has sudo permissions.
if operatingSystem == "Windows":
  # Log the installation of Cordova on Windows.
  print("Installing Cordova for Windows...")
  if os.system("npm install -g cordova") == 0:
    # Log the successful installation of Cordova on Windows.
    print("Cordova has been successfully installed on Windows.")
  else:
    # Log the unsuccessful installation of Cordova on Windows.
    print("Cordova failed to install on Windows.")
elif operatingSystem == "Linux" or operatingSystem == "Darwin":
  # Log the installation of Cordova on Linux or macOS.
  print("Installing Cordova for Linux or macOS...")
  if os.system("sudo npm install -g cordova") == 0:
    # Log the successful installation of Cordova on Linux or macOS.
    print("Cordova has been successfully installed on Linux or macOS.")
  else:
    # Log the unsuccessful installation of Cordova on Linux or macOS.
    print("Cordova failed to install on Linux or macOS.")
