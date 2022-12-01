# This code installs deskgap using the bun package manager.
# It determines the operating system and installs the package accordingly.
# The function names are install_deskgap_windows, install_deskgap_linux, and install_deskgap_other.
# The variable names are operatingSystem.
# It uses the operating system module and os module.

import os # Import os to use operating system commands
import platform # Import platform to get the operating system

# Get the operating system
operatingSystem = platform.system()

def install_deskgap_windows():
  # Install deskgap on Windows
  print("Installing Deskgap on Windows")
  os.system("bun install --save-dev deskgap")

def install_deskgap_linux():
  # Install deskgap on Linux
  print("Installing Deskgap on Linux")
  os.system("sudo bun install --save-dev deskgap")

def install_deskgap_other():
  # Install deskgap on other operating systems
  print("Installing Deskgap on other operating systems")
  os.system("bun install --save-dev deskgap")

# Install deskgap using bun
if operatingSystem == "Windows":
  # Install deskgap on Windows
  install_deskgap_windows()
elif operatingSystem == "Linux":
  # Install deskgap on Linux
  install_deskgap_linux()
else:
  # Install deskgap on other operating systems
  install_deskgap_other()
