import login as L

def setupPage():
    import os
    import time
    from os import system

    system('clear')

    with open('data/info.data', 'w') as f:
        f.writelines("1")

    print("""
    Bear OS v0.1.1
    Bear OS Registration
    """)

    usrname = input("Please enter your new username: ")
    pas = input("Please enter your new password: ")

    with open('data/username.pass', 'w') as f:
        f.writelines(usrname)

    with open('data/password.pass', 'w') as f:
        f.writelines(pas)

    print("Registration Complete...")
    print("Opening Login...")
    time.sleep(0.5)
    L.loginPage()