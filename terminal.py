import home as H
import os
import rootTerminal as RT
import time

login_pass = open('data/password.pass')
login_name = open('data/username.pass')
l_p = login_pass.read()
l_n = login_name.read()

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

def terminalMain():
    os.system('clear')
    print("Welcome to the Bear OS Terminal")
    print("Ver 1.2.3")
    def helpCom():
        os.system('clear')
        print("""
        Exit: Returns you to menu
        UserInfo: Tells you current user's information
        Root: Allows root terminal access

        More commands to come with future updates:
        """)

    while True:
        bruhVariable = input(f"{bcolors.OKBLUE}Bear OS >>{bcolors.OKGREEN} ")

        if bruhVariable == "Help":
            os.system('clear')
            helpCom()
        elif bruhVariable == "help":
            os.system('clear')
            helpCom()

        elif bruhVariable == "Exit":
            os.system('clear')
            H.homePage()
            break
        elif bruhVariable == "exit":
            os.system('clear')
            H.homePage()
            break

        elif bruhVariable == "UserInfo":
            os.system('clear')
            b_login = input(str("Please Enter The Password To " + l_n + " To view this data: "))
            if b_login == l_p:
                print("Username: " + l_n)
                print("Password: " + l_p)
            else:
                print("Wrong password")

        elif bruhVariable == "userinfo":
            os.system('clear')
            b_login = input(str("Please Enter The Password To " + l_n + " To view this data: "))
            if b_login == l_p:
                print("Username: " + l_n)
                print("Password: " + l_p)
            else:
                print("Wrong password")

        elif bruhVariable == "root":
            login = input("To access the root terminal, please enter your password: ")

            if login == l_p:
                dec = input(f"{bcolors.FAIL}Are you sure you want to enter the root terminal?{bcolors.HEADER} ")
                if dec == 'y':
                    RT.rootTerm()
                elif dec == 'Y':
                    RT.rootTerm()
                elif dec == 'n':
                    print("Returning to regular terminal...")
                    time.sleep(0.5)
                    terminalMain()
                elif dec == 'N':
                    print("Returning to regular terminal...")
                    time.sleep(0.5)
                    terminalMain()

        elif bruhVariable == "Root":
            login = input("To access the root terminal, please enter your password: ")

            if login == l_p:
                dec = input("Are you sure you want to enter the root terminal? ")
                if dec == 'y':
                    RT.rootTerm()
                elif dec == 'Y':
                    RT.rootTerm()
                elif dec == 'n':
                    print("Returning to regular terminal...")
                    time.sleep(0.5)
                    terminalMain()
                    break
                elif dec == 'N':
                    print("Returning to regular terminal...")
                    time.sleep(0.5)
                    terminalMain()
                    break

            elif login != l_p:
                print("Wrong password!")

        elif bruhVariable == "clear":
            os.system('clear')

        elif bruhVariable == "Clear":
            os.system('clear')

        else:
            print("The command, " "" + bruhVariable + "" " wasn't found!")