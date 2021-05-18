"""ToDo:  
encrypted file for data table
data table; account name, username, password, url?
search data table
stronger login
menus as functions?
menu items as functions?
COMMENTS!
"""

import codecs
import os
import os.path
import string
import random
from random import shuffle
import csv

DefaultSize = "mode con: cols=100 lines=20"
os.system(DefaultSize)

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

def logo():
    print('________                     __________  __\n___  __ \_____ _________________  __ \ \/ /\n__  /_/ /  __ `/_  ___/_  ___/_  /_/ /_  / \n_  ____// /_/ /_(__  )_(__  )_  ____/_  /  \n/_/     \__,_/ /____/ /____/ /_/     /_/   \n\n\n\n\n')

def header():
    clrscr()
    os.system(DefaultSize)
    logo()

def PassGen():
    x = 0
    while x < 3:
        x=int(input("1:  Have PassPY generate a password with a length you choose\n2:  Type your own password\n"))
        if x == 1:
            header()
            length = float(input("How many characters would you like the password to be?  \n"))
            div = int(length/3)
            r = int(length%3)
            seed = string.ascii_letters    # Generating letters
            letters = ( ''.join(random.choice(seed) for i in range(div)) )

            seed = string.digits    # generating digits
            numbers = ( ''.join(random.choice(seed) for i in range(div)) )

            seed = string.punctuation    # generating punctuation
            punctuation = ( ''.join(random.choice(seed) for i in range(div + r)) )

            hold = letters + numbers + punctuation
            PassGen.password = ( ''.join(random.sample(hold, len(hold))))
            print("here is the generated password, do not forget it:  " + PassGen.password)
            input("press Enter once the password is memorized (dont worry if you forget, it was saved in your password directory.)\n")
            return
        elif x == 2:
            header()
            PassGen.password = input("Type the password, then press Enter: \n")
            return
        else:
            return


#Startup Phase
header()
print("Welcome to PassPY, the python based, opensource password...")
start = input("Press ENTER to start")

login = 0
while login < 3:
    header()
    print("Welcome!\n *UNDER CONSTRUCTION* 1:  New users - register your account\n 2:  Existing users - log in\n 3:  Exit - close the application.")
    login = int(input("Enter a number:\n"))
#registration
    if login == 1:
        header()
        print("New user registration is curently under construction")
        #print("user name rules:\n1: ")
        NewUserLogin = input("Enter Username:  ")
        nametest1 = NewUserLogin + "login" + ".txt"
        try:
            usersearch = open(nametest1)  #search for user's password file
            usersearch.close()
            header()
            print("User name not available")
            #print("user name rules:\n1: ")
            NewUserLogin = input("Try another Username:  ")
            nametest1 = NewUserLogin + "login" + ".txt"
        except FileNotFoundError:
            header()
            print("User name is available")
            
        create = open(nametest1,"a")  #create user's password file
        #password = input("Enter password:  ")
        password1 = input("enter desired password:")
        cypher = codecs.encode(password1, 'ROT13')
        create.write(cypher)
        create.close()
        print("Done!  New account created!\nWelcome.")
   

    elif login == 2:
        
        #Login Process
        header()
        user_name = input("Enter Username: ")
        nametest2 = user_name + "login" + ".txt"
        try:
            usersearch = open(nametest2,"r")  #search for user's password file
            lst = list(usersearch.readlines())
            confirm = lst[-1]
            print("Hello " + user_name)
            password = input("Enter Password: ")
            compare = codecs.encode(password, 'ROT13')

            if compare == confirm:
                print("Access Granted")
            else:
                print("else triggered.  Access Denied")
                exit(exit())
        except FileNotFoundError:
            header()
            print("Access Denied")
            input("please press enter to continue")
            exit(exit())
       
        nametest3 = user_name + "passwords" + ".txt"
        
        menu = 0
        while menu < 4:
            header()
            print("Menu:\n  1:  New password - register new password\n  2:  List - show passwords\n  3:  *UNDER CONSTRUCTION* Register new user - create another user account\n  4:  Exit")
            menu = int(input("Enter a number:\n"))
            if menu == 1:
                header()
                filea = open(user_name + "passwords" + ".txt","a")
                PassGen()
                #inputask = input("Input new password: ")
                cypher = codecs.encode(PassGen.password, 'ROT13')
                filea.write("\n" + cypher)
                filea.close()
                print("Done!")
            elif menu == 2:
                #logo()
                filer = open(nametest3,"r") #"a+" isn't reading the file
                contents = filer.read()
                plaintext = codecs.encode(contents, 'ROT13')
                count = contents.splitlines()
                ReadSize = "mode con: cols=100 lines=" + str(int(len(count)) + 13)
                os.system(ReadSize)
                logo()
                input("Current Passwords: \n(Press Enter to continue)\n" + plaintext)
                filer.close()
            elif menu == 3:
                header()
                print("New user registration is curently under construction.\n Menu:\n  1:  new password - register new password\n  2:  list - show passwords\n  4:  Exit")
                menu = int(input("Enter a number:\n"))
            elif menu == 4:
                clrscr()
                exit()
    elif login == 3:
        clrscr()
        exit()