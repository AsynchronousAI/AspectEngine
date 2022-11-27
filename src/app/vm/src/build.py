# This script creates a new project folder and installs the dependencies
# It is used to create a new project in the projects directory
# The name of the project is passed in as a command line argument
# It uses a main function that calls other functions
# The main function calls the create_project function
# The create_project function calls another function called install_dependencies
# The install_dependencies function uses the os.system function to install the dependencies

import os
import sys
from typing import List

def create_project(project_name: str) -> None:
    """Creates a new project folder and installs the dependencies."""
    print(f"Creating project {project_name}")

    # change the working directory to the project folder
    os.chdir(project_name)

    # install the dependencies
    install_dependencies()

    # go back to the parent directory
    os.chdir("..")

def install_dependencies():
    """Installs the dependencies."""
    print("Installing dependencies")

    # install the dependencies using the npm install command
    os.system("npm install")

def main():
    """The main function of the script."""
    # get the project name from the command line arguments
    project_name: str = sys.argv[1:][0]

    # call the create_project function
    create_project(project_name)

if __name__ == "__main__":
    main()