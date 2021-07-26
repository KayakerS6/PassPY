import codecs
import os
import os.path
import string
import random
from random import shuffle
import csv
import time
import hashlib

DefaultSize = "mode con: cols=100 lines=20"
os.system(DefaultSize)

pre = "C:\ProgramData\PassPY"
if not os.path.exists(pre):
    os.makedirs(pre)

account = ""
cypher = ""
username = ""
user_name = ""
m = ""

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

def logo():
    print("________                     __________  __\n___  __ \_____ _________________  __ \ \/ /\n__  /_/ /  __ `/_  ___/_  ___/_  /_/ /_  / \n_  ____// /_/ /_(__  )_(__  )_  ____/_  /  \n/_/     \__,_/ /____/ /____/ /_/     /_/   \n\n\n\n\n")

def header():
    clrscr()
    os.system(DefaultSize)
    logo()

def PassGen(user_name,account,username,pre):
    x = 0
    while x < 3:
        x=int(input("1:  Have PassPY generate a password with a length you choose\n2:  Type your own password\n"))
        if x == 1:
            header()
            length = float(input("How many characters would you like the password to be?  \n"))
            div = int(length/3)
            r = int(length%3)
            seed = string.ascii_letters    # Generating letters
            letters = ( ''.  join(random.choice(seed) for i in range(div)) )

            seed = string.digits    # generating digits
            numbers = ( ''.join(random.choice(seed) for i in range(div)) )

            seed = string.punctuation    # generating punctuation
            punctuation = ( ''.join(random.choice(seed) for i in range(div + r)) )

            hold = letters + numbers + punctuation
            PassGen.password = ( ''.join(random.sample(hold, len(hold))))
            account = codecs.encode(account, 'ROT13')
            username = codecs.encode(username, 'ROT13')
            PassGen.password = codecs.encode(PassGen.password, 'ROT13')
            newline = account + "\t" + username + "\t" + PassGen.password
            post = user_name + "passwords" + ".csv"
            location = os.path.join(pre, post)
            with open(location, "a", newline="\n") as filea:
                filea.write(newline + "\n")
            print("here is the generated password:  " + PassGen.password)
            input("press Enter once the password is memorized (dont worry if you forget, it was saved in your password directory.)\n")
            MainMenu(user_name)
        elif x == 2:
            header()
            PassGen.password = input("Type the password, then press Enter: \n")
            account = codecs.encode(account, 'ROT13')
            username = codecs.encode(username, 'ROT13')
            PassGen.password = codecs.encode(PassGen.password, 'ROT13')
            newline = account + "\t" + username + "\t" + PassGen.password
            post = user_name + "passwords" + ".csv"
            location = os.path.join(pre, post)
            with open(location, "a", newline="\n") as filea:
                filea.write(newline + "\n")
            MainMenu(user_name)
        else:
            Signin()

def Signin(pre):
    header()
    user_name = input("Enter Username: ")
    nametest2 = user_name + "login" + ".txt"
    location = os.path.join(pre, nametest2)
    try:     #check to see if the account exists
        usersearch = open(location,"r")  #search for user's password file
        lst = list(usersearch.readlines())
        confirm = lst[-1]
        print("Hello " + user_name)
        password = input("Enter Password: ")
        hold = hashlib.sha256(password.encode('utf-8'))
        compare = hold.hexdigest()
        if compare == confirm:
            print("Access Granted")
            MainMenu(user_name)
        else:
            print("Access Denied")
            Signin(pre)
    except FileNotFoundError:
        header()
        print("Username not found!")
        input("please press enter to continue")
        Login(pre)

def AddEntry(user_name,pre):
    header()
    account = input("what account is this password for? (e.g. GitHub)\n")
    username = input("What is the username for " + account + "?\n")
    PassGen(user_name,account,username,pre)
    print("Done!")

def PasswordSearch(user_name,pre):
    c = ""
    header()
    post = user_name + "passwords" + ".csv"
    location = os.path.join(pre, post)
    SearchColumn = int(input("Password Search Menu:\nPress 1 to show all passwords\nPress 2 to search by account\nPress 3 to search by username\nPress 4 to search by password\nPress 5 to return to the Main Menu\n   "))
    try:     #make sure there is a password file to search through
        with open(location) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            if SearchColumn == 1:  
                header()
                print("Here are all of the stored passwords:  ")
                for row in csv_reader:
                    print(codecs.encode(row[2], 'ROT13'))
                m = input("Press Enter to continue to the Main Menu")
                MainMenu(user_name)
            elif SearchColumn == 2:
                header()
                search = input("What Account are you looking for?  \n")
                for row in csv_reader:
                    if codecs.encode(search, 'ROT13') == row[0]:
                        header()
                        c = int(input("The Account, Username and Password information for " + codecs.encode(row[0], 'rot13') + " are:\n" + codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13') + "\nEnter 1 if you want to copy the password to the clipboard\nEnter 2 if you do not\n"))
                        if c == 1:
                            target = codecs.encode(row[2], 'ROT13')
                            header()
                            print("The Account, Username and Password information for " + codecs.encode(row[0], 'rot13') + " are:\n" + codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13'))
                            Clipboard(target)
                            MainMenu(user_name)
                        elif c == 2:
                            m = input("Password NOT copied, Press enter to continue looking")
                            continue
                        else:
                            m = input("Password NOT copied, Press enter to return to the Main Menu")
                            MainMenu(user_name)
                MainMenu(user_name)
            elif SearchColumn == 3:
                header()
                search = input("What Username are you looking for?  \n")
                for row in csv_reader:
                    if codecs.encode(search, 'ROT13') == row[1]:
                        c = int(input(codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13') + "\nEnter 1 if you want to copy the password to the clipboard\nEnter 2 if you do not\n"))
                        if c == 1:
                            target = codecs.encode(row[2], 'ROT13')
                            header()
                            print("The Account, Username and Password information for " + codecs.encode(row[0], 'rot13') + " are:\n" + codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13'))
                            Clipboard(target)
                            MainMenu(user_name)
                        elif c == 2:
                            m = input("Password NOT copied, Press enter to return to continue searching")
                            continue
                        else:
                            m = input("Password NOT copied, Press enter to return to the Main Menu")
                            MainMenu(user_name)
                    MainMenu(user_name)
            elif SearchColumn == 4:
                header()
                search = input("What password are you looking for?  \n")
                for row in csv_reader:
                    if codecs.encode(search, 'ROT13') == row[2]:
                        c = int(input(codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13') + "\nEnter 1 if you want to copy the password to the clipboard\nEnter 2 if you do not\n"))
                        if c == 1:
                            target = codecs.encode(row[2], 'ROT13')
                            header()
                            print("The Account, Username and Password information for " + codecs.encode(row[0], 'rot13') + " are:\n" + codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13'))
                            Clipboard(target)
                            MainMenu(user_name)
                        elif c == 2:
                            m = input("Password NOT copied, Press enter to return to continue")
                            continue
                        else:
                            m = input("Password NOT copied, Press enter to return to the Main Menu")
                            MainMenu(user_name)
                    MainMenu(user_name)
            elif SearchColumn == 5:
                MainMenu(user_name)
            else:
                m = input("enter 1, 2, 3 or 4:\n")
                PasswordSearch(user_name)
    except FileNotFoundError:
        header()
        print("Please register some passwords for me to search through.")
        input("please press enter to continue")
        MainMenu(user_name)

def Clipboard(target):
    command = 'echo ' + target.strip() + '| clip'
    os.system(command)
    time.sleep(1)
    print("The clipboard will be cleared in 5 seconds")
    time.sleep(1)
    print("The clipboard will be cleared in 4 seconds")
    time.sleep(1)
    print("The clipboard will be cleared in 3 seconds")
    time.sleep(1)
    print("The clipboard will be cleared in 2 seconds")
    time.sleep(1)
    print("The clipboard will be cleared in 1 seconds")
    time.sleep(1)
    print("The clipboard will be cleared now")
    os.system("echo.| clip")

def MainMenu(user_name):
    header()
    print("Menu:\n  1:  New password - register new password\n  2:  List - show passwords\n  3:  Exit")
    menu = int(input("Enter a number:\n"))
    if menu == 1:
        AddEntry(user_name,pre)
    elif menu == 2:
        PasswordSearch(user_name,pre)
    elif menu == 3:
        clrscr()
        exit()
    else:
        MainMenu(user_name)

def Register(pre):
    header()
    user_name = input("Enter Username:  ")
    nametest1 = user_name + "login" + ".txt"
    location = os.path.join(pre, nametest1)
    try:
        usersearch = open(location)  #search for user's password file
        usersearch.close()
        header()
        print("User name not available")
        input("Press Enter to try again:  ")
        Register()
    except FileNotFoundError:
        header()
        print("User name is available")
        create = open(location,"a")  #create user's password file
        password1 = input("enter desired password:\n")
        pt = hashlib.sha256(password1.encode('utf-8'))
        cypher = pt.hexdigest()
        create.write(cypher)
        create.close()
        header()
        input("Done!  \nNew account created!\nWelcome!")
        MainMenu(user_name)

def Login(pre):
    header()
    print("Welcome!\n 1:  New users - register your account\n 2:  Existing users - log in\n 3:  Exit - close the application.")
    login = int(input("Enter a number:\n"))
    if login == 1:
        Register(pre)
    elif login == 2:
        Signin(pre)
    elif login == 3:
        clrscr()
        exit()
    else:
        Login()

#Startup Phase
header()
print("Welcome to PassPY, the python based, opensource password storage\nIf you like PassPY, share it with a friend github.com/kayakers6/passpy\nIf you love PassPY, BTC:  bc1qsqc3v2jt3lh0kq9addf4gu6e2uq5vxxfk35pl\n                    SNX:  0x05E8813B7dc3c4e039D898CB13f21A6E4d675bc1")
start = input("Press ENTER to start")
Login(pre)
