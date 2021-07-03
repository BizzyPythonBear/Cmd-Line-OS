import os
import login as L
import setup as S
from os import system

system('clear')
data_info = open('data/info.data')
data = data_info.read()

if data == '0':
    print("Welcome to Bear's command line OS!")
    print("Since you are a new user, I will open the register page for you.")
    S.setupPage()

if data == '1':
    print("Welcome back to Bear's command line OS!")
    L.loginPage()