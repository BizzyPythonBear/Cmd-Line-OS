import os
import home as H

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

def rootTerm():
    os.system('clear')
    print(f"{bcolors.OKCYAN}Welcome to the Bear OS Terminal")
    print("Ver 1.2.4")
    print("You're in the ROOT terminal, enter command 'exit' to return to menu.")
    def helpCom():
        os.system('clear')
        print("""
        Exit: Returns you to menu
        UserInfo: Tells you current user's information
        python3: Allows you to run .py files
        clear: Clears screen

        More commands to come with future updates:
        """)

    while True:
        bruhVariable = input(f"(ROOT) Bear OS >> {bcolors.OKGREEN}")
        print(f"{bcolors.OKCYAN}")
        if bruhVariable == "Help":
            os.system('clear')
            helpCom()
        elif bruhVariable == "help":
            os.system('clear')
            helpCom()

        if bruhVariable == "Exit":
            os.system('clear')
            H.homePage()
            break
        elif bruhVariable == "exit":
            os.system('clear')
            H.homePage()
            break

        if bruhVariable == "UserInfo":
            os.system('clear')
            print("Username: " + l_n)
            print("Password: " + l_p)

        elif bruhVariable == "userinfo":
            os.system('clear')
            print("Username: " + l_n)
            print("Password: " + l_p)

        elif bruhVariable == "python3":
            m = input("What file would you like to run? ")
            if m.endswith('.py'):
                os.system(f'python3 {m}')
            else:
                print(m + " is not a py file.")

        else:
            print("The command, " "" + bruhVariable + "" " wasn't found!")