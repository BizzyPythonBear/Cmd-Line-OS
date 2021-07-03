import home as H
import os

login_pass = open('data/password.pass')
login_name = open('data/username.pass')
l_p = login_pass.read()
l_n = login_name.read()

def terminalMain():
    os.system('clear')
    print("Welcome to the Bear OS Terminal")
    print("Ver 0.1.1")
    def helpCom():
        os.system('clear')
        print("""
        Exit: Returns you to menu
        UserInfo: Tells you current user's information

        More commands to come with future updates:
        """)

    while True:
        bruhVariable = input("Bear OS >> ")

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
            b_login = input(str("Please Enter The Password To " + l_n + " To view this data: "))
            if b_login == l_p:
                print("Username: " + l_n)
                print("Password: " + l_p)
            else:
                print("Wrong password")

        elif bruhVariable == "userinfo":
            os.system('clear')
            b_login = input(str("Please Enter The Password To " + l_n + " To Open BioS: "))
            if b_login == l_p:
                print("Username: " + l_n)
                print("Password: " + l_p)
            else:
                print("Wrong password")

        else:
            print("The command, " "" + bruhVariable + "" " wasn't found!")