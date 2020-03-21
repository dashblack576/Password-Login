#! /usr/bin/local/python3/

import os
import password_maker
import time

class New_Account:
    def __init__(self, password, email):
        global password_list
        global email_list
        self.password = password
        password_list = []
        password_list.append(password)

        self.email = email
        email_list = []

class Login:
        def __init__(self, password, email):
            self.password = password
            self.email = email
            
            if password in password_list and email in email_list:
                print("Access Granted")
                os.system('clear')
                os.system('ls')
                
                file_ = input("Which file do you want to run?\n>>>")
                
                if file_ =="password_maker":
                    password_maker.main()

                else:
                    print("Not a file or you do not have the right to  access that file")
            else:
                print("Access Denied")

master = str(123456789)

os.system('clear')

while True:
    cheak = input(">>>")
    if cheak =="Login" or cheak == "login":
        name = input("What is your name?\n>>>")
        email = input("What is your email?\n>>>")
        password = input("What is your password\n>>>")
        name = Login(password, email)

    elif cheak =="New Account" or cheak =="new_account":
        mast = input("What is the master password?\n>>>")
        if mast == master:
            name = input("What is your name?\n>>>")
            email = input("What is your email?\n>>>")
            password = input("What is your password\n>>>")
            name = New_Account(password, email)

    if cheak =="Stop" or cheak =="stop":
        os.system('clear')
        break

    else:
        print("Not Applicable")
           
        











































