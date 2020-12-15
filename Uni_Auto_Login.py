# Run
# Check if Chrome is already opened or not
# Open Chrome in private mode
# Make full screen
# Go to UniSA page (https://my.unisa.edu.au/student/portal/)
# Enter username and password
# Sign in

""" Uni_Auto_Login.

A python script that automatically signs into University's student portal and opens new tab to email sign in page.

"""

__author__ = 'Anthony T Nguyen'
__version__ = '1.0.0'
__date__ = '15.12.2019'

import subprocess
import os
import time
import pyautogui

def open_Chrome():
    """ Opens Google Chrome

    Function that opens the Google Chrome web browser in incognito mode.

    """

    try:
        subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", "my.unisa.edu.au/student/portal/"])
        iteration = 0
        print("Searching for 1st SignIn Icon...")
        while True:
            iteration += 1
            SignInIconCoord = pyautogui.locateOnScreen('F:\_Installation\_Portalable_Python\_python_root\Single_file_projects\Auto_Login\SignInIcon.png')
            if (SignInIconCoord != None):
                print(SignInIconCoord)
                break
            # Every 10th count will cause the program to refresh.
            elif (iteration % 10 == 0):
                print('Refreshing...')
                pyautogui.hotkey('f5')
            else:
                print('Searching...', iteration)

        # Enter login details for the current input boxes.
        login_details()

        print("Searching myMail Icon...")
        while True:
            iteration += 1
            myMailIcon = pyautogui.locateOnScreen('F:\_Installation\_Portalable_Python\_python_root\Single_file_projects\Auto_Login\myMailIcon.png')
            if (myMailIcon != None):
                print(myMailIcon)
                break
            else:
                print('Searching...', iteration)
        
        myMailCenterCoords = pyautogui.center(myMailIcon)
        myMailIconX = myMailCenterCoords[0]
        myMailIconY = myMailCenterCoords[1]
        pyautogui.click(myMailIconX, myMailIconY, button='right')
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl', 'tab')

        print("Searching for 2nd SignIn Icon...")
        while True:
            iteration += 1
            SignInIconCoord2 = pyautogui.locateOnScreen('F:\_Installation\_Portalable_Python\_python_root\Single_file_projects\Auto_Login\SignInIcon-2.png')
            if (SignInIconCoord2 != None):
                print(SignInIconCoord2)
                break
            else:
                print('Searching...', iteration)
        
        # Enter login details for the current input boxes.
        login_details()
        print("Successful Login")

    except Exception as errorMsg:
        print(errorMsg)

def login_details():
    """ Login details function

    Function that stores the necessary authentication details to log in. 

    """
    username = ''
    password = ''

    # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
    script_location = os.path.dirname(os.path.abspath(__file__))
    abs_file_path = os.path.join(script_location, "QuI.NTH")
    print(abs_file_path)
    new_file = os.path.join(script_location, "QuI.NTH.txt")
    print(new_file)
    if (os.path.exists(abs_file_path)):
        os.rename(abs_file_path, new_file)
        print("[+] Renamed")
        # Will not load all contents of the file into memory.
        with open(new_file) as input_file:
            lines = input_file.readlines()
            index = 0
            for current_line in lines:
                if (index == 0):
                    username = current_line.strip()
                if (index == 1):
                    password = current_line.strip()
                index += 1
        input_file.close()
        print("Closed file")
        os.rename(new_file, abs_file_path)
        print("Renamed again")
    else:
        print("[-] Login file not found")
        exit(0)

    # Enter your username here.
    pyautogui.typewrite(username)
    pyautogui.hotkey('tab')

    # Enter your password here.
    pyautogui.typewrite(password)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')

def main():
    """
    Begin
    """
    open_Chrome()

if __name__ == "__main__":
    main()
