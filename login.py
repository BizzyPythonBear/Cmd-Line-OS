def loginPage():
    import os
    import time
    import home as H
    from os import system
    import rootTerminal as RT
    import devTerminal as DT

    system('clear')

    login_pass = open('data/password.pass')
    login_name = open('data/username.pass')
    l_p = login_pass.read()
    l_n = login_name.read()
    print("""
    Bear OS v1.2.3
    Bear OS Login Screen
    """)

    while True:
        log = input("Enter Password To " + l_n + " To Login: ")

        if log == l_p:
            print("Opening Home Page...")
            time.sleep(0.5)
            system('clear')
            H.homePage()
            break

        elif log == "559907":
            print("Developer Mode Activated...")
            time.sleep(0.5)
            system('clear')
            H.devPage()
            break

        elif log == "559908":
            print("Taking you to root dev console...")
            time.sleep(0.5)
            system('clear')
            DT.devTermMain()
            break


        else:
            print("Wrong Passowrd To " + l_n)