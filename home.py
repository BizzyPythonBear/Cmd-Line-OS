
import time
import os
import socket
from os import system
import terminal as T
import editor as E

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
    print("""
    Bear OS v0.1.1
    Home page

    """)
    print("Welcome " + l_n)
    print("The Date Is: " + time.strftime("%m/%d/%y"))
    print("""
    [1] To Open Google
    [2] To Open Text Editor
    [3] To Open File Exploer
    [4] To Configure and Open BioS
    [5] To Open Terminal
    [6] To Open Calculator
    [7] To Close OS Safley
    """)

    select = input("[?]: ")

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
            b_login = input(str("Please Enter The Password To " + l_n + " To Open BioS: "))
            if b_login == l_p:
                print("Opening BioS")
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
                    os.startfile('home.py')
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
                    print("Leaving BIOS...")
                    time.sleep(0.5)
                    homePage()
                    break

                if edit_b == 'e':
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
        os.system('exit')

    else:
        error()

clearDumbScreen()