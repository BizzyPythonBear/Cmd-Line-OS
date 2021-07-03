
import time
import os
import socket
from os import system
import terminal as T
import editor as E
import sys
import devTerminal as DTM

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clearDumbScreen():
    system("clear")

def error():
    system('clear')
    print("This action doesn't exist, or hasn't been implemented yet.")
    homePage()

def homePage():
    login_pass = open('data/password.pass')
    login_name = open('data/username.pass')
    l_p = login_pass.read()
    l_n = login_name.read()
    print(f"""{bcolors.OKBLUE}
    Bear OS v1.2.4
    Home page

    """)
    print(f"{bcolors.OKBLUE}Welcome " + l_n)
    print(f"{bcolors.OKBLUE}The Date Is: " + time.strftime("%m/%d/%y"))
    print(f"""{bcolors.OKBLUE}
    [1] To Open Google
    [2] To Open Text Editor
    [3] To Open File Exploer
    [4] To Configure and Open BioS
    [5] To Open Terminal
    [6] To Open Calculator
    [7] Show Recent Updates
    [8] To restart the system
    [9] To Close OS Safley
    """)

    select = input(f"[?]:{bcolors.OKGREEN} ")
    print(f"{bcolors.OKBLUE}")

    if select == '1':
        print("Called")
        error()

    elif select == '2':
        clearDumbScreen()
        E.editorMain()

    elif select == '3':
        error()

    elif select == '4':
        system('clear')
        while True:
            b_login = input(str("Please Enter The Password To " + l_n + " To Open BioS: "))
            if b_login == l_p:
                print("Opening BioS")
                print("Press enter the command 'e' to exit")
                host_name = socket.gethostname()
                host_ip = socket.gethostbyname(host_name)
                print("[1] USER NAME: " + l_n)
                print("[2] PASSWORD: " + l_p)
                print("Hostname:", host_name)
                print("LOCAL IPS: " + host_ip)
                edit_b = input("Enter [?] to change setting: ")
                if edit_b == '1':
                    edit_n = input("Enter New Username: ")
                    with open('data/username.pass', 'w') as f:
                        f.writelines(edit_n)
                    print("Username Changed To " + edit_n)
                    input("Press Enter To Restart: ")
                    homePage()
                    os.system('exit')

                if edit_b == '2':
                    edit_p = input("Enter New Password: ")
                    with open('data/password.pass', 'w') as f:
                        f.writelines(edit_p)

                    print("Password Changed To " + edit_p)
                    input("Press Enter To Restart: ")
                    homePage()
                    os.system('exit')

                if edit_b == 'E':
                    os.system('clear')
                    print("Leaving BIOS...")
                    time.sleep(0.5)
                    homePage()
                    break

                if edit_b == 'e':
                    os.system('clear')
                    print("Leaving BIOS...")
                    time.sleep(0.5)
                    homePage()
                    break

                else:
                    print("You can't change that!")

            else:
                print("Wrong Password To " + l_n)

    elif select == '5':
        clearDumbScreen()
        T.terminalMain()

    elif select == '6':
        error()

    elif select == '7':
        clearDumbScreen()
        print(f"""
{bcolors.OKBLUE}Update 1.2.4:
    {bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Terminal Based text editor soon!
    {bcolors.OKGREEN}[+] You can now run .py files from the terminal
{bcolors.OKBLUE}Update 1.2.3:
    {bcolors.OKGREEN}[+] Bug Fixes
    [+] Ability to Restart
    {bcolors.FAIL}[-] The browser feature wont be able to work for a while
{bcolors.OKBLUE}Update 1.2.2:
    {bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Big Change with Menu Coming Soon!
    {bcolors.OKGREEN}[+] Cosmetics
    [+] Colors
        {bcolors.FAIL}[-] Not Enough Colors
    {bcolors.OKGREEN}[+] Minor Bug Fixes
{bcolors.OKBLUE}Update 1.2.1:
    {bcolors.OKGREEN}[+] Added Developer mode
    [+] Bug Fixes
    [+] Better Error Handling
{bcolors.OKBLUE}Update 0.2.1:
    {bcolors.OKGREEN}[+] Bug Fixes
{bcolors.OKBLUE}Update 0.0.1:
    {bcolors.OKGREEN}[+] Basic Files Added
        {bcolors.FAIL}[-] Lots Of Bugs
{bcolors.OKBLUE}--------------------------------------------
{bcolors.OKBLUE}Full github repository: {bcolors.OKGREEN}https://github.com/BizzyPythonBear/Cmd-Line-OS
{bcolors.OKBLUE}--------------------------------------------
{bcolors.FAIL}Press 'e' to exit
        """)
        while True:
            thing = input("Command: ")
            if thing == 'e':
                os.system('clear')
                homePage()
                break

            elif thing == 'E':
                os.system('clear')
                homePage()
                break
            
            else:
                print("That isn't an 'e'.")

    elif select == '8':
        print("Restarting...")
        time.sleep(1)
        exec(open('BearCMDos.py').read())

    elif select == '9':
        print("Shutting down...")
        print("Have a nice day!")
        time.sleep(1)
        os.system('exit')
        sys.exit()
    else:
        error()

def devPage():
    login_pass = open('data/password.pass')
    login_name = open('data/username.pass')
    l_p = login_pass.read()
    l_n = login_name.read()
    print(f"""{bcolors.OKBLUE}
    Bear OS v1.2.4
    Home page
    (DEVELOPER MODE: ACTIVATED)

    """)
    print(f"{bcolors.OKBLUE}Welcome, Admin")
    print(f"{bcolors.OKBLUE}The Date Is: " + time.strftime("%m/%d/%y"))
    print(f"""{bcolors.OKBLUE}
    [1] To Open Google
    [2] To Open Text Editor
    [3] To Open File Exploer
    [4] To Configure and Open BioS
    [5] To Open Terminal
    [6] To Open Calculator
    [7] To Show Recent Updates
    [8] To restart the system
    [9] To Close OS Safley
    """)

    select = input(f"[?]:{bcolors.OKGREEN} ")
    print(f"{bcolors.OKBLUE}")
    if select == '1':
        error()

    elif select == '2':
        clearDumbScreen()
        E.editorMain()

    elif select == '3':
        error()

    elif select == '4':
        system('clear')
        while True:
            print("Opening BioS")
            print("Press enter the command 'e' to exit")
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print("[1] USER NAME: " + l_n)
            print("[2] PASSWORD: " + l_p)
            print("Hostname:", host_name)
            print("LOCAL IPS: " + host_ip)
            edit_b = input("Enter [?] to change setting: ")
            if edit_b == '1':
                edit_n = input("Enter New Username: ")
                with open('data/username.pass', 'w') as f:
                    f.writelines(edit_n)
                print("Username Changed To " + edit_n)
                input("Press Enter To Restart: ")
                homePage()
                os.system('exit')

            if edit_b == '2':
                edit_p = input("Enter New Password: ")
                with open('data/password.pass', 'w') as f:
                    f.writelines(edit_p)
                print("Password Changed To " + edit_p)
                input("Press Enter To Restart: ")
                homePage()
                os.system('exit')

            if edit_b == 'E':
                os.system('clear')
                print("Leaving BIOS...")
                time.sleep(0.5)
                homePage()
                break

            if edit_b == 'e':
                os.system('clear')
                print("Leaving BIOS...")
                time.sleep(0.5)
                homePage()
                break

            else:
                print("You can't change that!")

    elif select == '5':
        clearDumbScreen()
        DTM.devTermMain()

    elif select == '6':
        error()

    elif select == '7':
        clearDumbScreen()
        print(f"""
{bcolors.OKBLUE}Update 1.2.4:
    {bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Terminal Based text editor soon!
    {bcolors.OKGREEN}[+] You can now run .py files from the terminal
{bcolors.OKBLUE}Update 1.2.3:
    {bcolors.OKGREEN}[+] Bug Fixes
    [+] Ability to Restart
    {bcolors.FAIL}[-] The browser feature wont be able to work for a while
{bcolors.OKBLUE}Update 1.2.2:
    {bcolors.OKBLUE}[{bcolors.OKCYAN}!{bcolors.OKBLUE}] Big Change with Menu Coming Soon!
    {bcolors.OKGREEN}[+] Cosmetics
    [+] Colors
        {bcolors.FAIL}[-] Not Enough Colors
    {bcolors.OKGREEN}[+] Minor Bug Fixes
{bcolors.OKBLUE}Update 1.2.1:
    {bcolors.OKGREEN}[+] Added Developer mode
    [+] Bug Fixes
    [+] Better Error Handling
{bcolors.OKBLUE}Update 0.2.1:
    {bcolors.OKGREEN}[+] Bug Fixes
{bcolors.OKBLUE}Update 0.0.1:
    {bcolors.OKGREEN}[+] Basic Files Added
        {bcolors.FAIL}[-] Lots Of Bugs
{bcolors.OKBLUE}--------------------------------------------
{bcolors.OKBLUE}Full github repository: {bcolors.OKGREEN}https://github.com/BizzyPythonBear/Cmd-Line-OS
{bcolors.OKBLUE}--------------------------------------------
{bcolors.FAIL}Press 'e' to exit
        """)
        while True:
            thing = input("Command: ")
            if thing == 'e':
                os.system('clear')
                devPage()
                break

            elif thing == 'E':
                os.system('clear')
                devPage()
                break
            
            else:
                print("That isn't an 'e'.")

    elif select == '8':
        print("Restarting...")
        time.sleep(1)
        exec(open('BearCMDos.py').read())

    elif select == '9':
        print("Shutting down...")
        print("Have a nice day!")
        time.sleep(1)
        os.system('exit')
        sys.exit()

    else:
        error()

clearDumbScreen()