def loginPage():
    import os
    import time
    import home as H
    from os import system

    system('clear')

    login_pass = open('data/password.pass')
    login_name = open('data/username.pass')
    l_p = login_pass.read()
    l_n = login_name.read()
    print("""
    Bear OS v0.1.1
    Bear OS Login Screen
    """)

    while True:
        log = input("Enter Password To " + l_n + " To Login: ")

        if log == l_p:
            print("Opening Home Page...")
            time.sleep(0.5)
            H.homePage()
            break

        else:
            print("Wrong Passowrd To " + l_n)