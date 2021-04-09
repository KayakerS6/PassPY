import codecs
import os
import os.path
import string
import random
from random import shuffle
import csv

'''def UserCheck():
    NewUser = input("Enter Username:  ")
    nametest = NewUser + ".txt"
    try:
        usersearch = open(nametest)  #search for user's password file
        usersearch.close()
        print(FileFoundStatement)
    except FileNotFoundError
        print(FileNotFoundStatement)'''

def PassGen():
    x = 0
    while x < 3:
        x=int(input("1:  Have PassPY generat a password with a length you choose\n2:  Type your own password\n"))
        if x == 1:
            length = float(input("How many characters would you like the password to be?  "))
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
            return
        elif x == 2:
            PassGen.password = input("Enter the password you would like to use: ")
            return
        else:
            return

#Startup Phase
print("Welcome to PassPY, the python based, opensource password...")
start = input("Press ENTER to start")

login = 0
while login < 3:
    print("Welcome!\n *UNDER CONSTRUCTION* 1:  New users - register your account\n 2:  Existing users - log in\n 3:  Exit - close the application.")
    login = int(input("Enter a number:\n"))
#registration
    if login == 1:
        print("New user registration is curently under construction")
        #print("user name rules:\n1: ")
        FileFoundStatement = "Username not avaliable"
        FileNotFoundStatement = "User created\nWelcome " + NewUser
        NewUser = input("Enter Username:  ")
        nametest = NewUser + ".txt"
        try:
            usersearch = open(nametest)  #search for user's password file
            usersearch.close()
            print("User name not available")
            #print("user name rules:\n1: ")
            NewUser = input("Try another Username:  ")
            nametest = NewUser + ".txt"
        except FileNotFoundError:
            print("User name is available")
            
        create = open(nametest,"a")  #create user's password file
        
        PassGen()
        cypher = codecs.encode(PassGen.password, 'ROT13')
        create.write(cypher)
        create.close()
        print("Done!  New account created!\nWelcome.")
 
    elif login == 2:
        
        #Login Process
        user_name = input("Enter Username: ")
        nametest = user_name + ".txt"
        try:
            usersearch = open(nametest,"r")  #search for user's password file
            lst = list(usersearch.readlines())
            confirm = lst[0]
            print("Hello " + user_name)
            password = input("Enter Password: ")
            compare = codecs.encode(password, 'ROT13')

            #the issue is between here
            if compare == confirm:
                print("Access Granted")
            else:
                print("else triggered.  Access Denied")
                exit(exit())
        except FileNotFoundError:
            print("Access Denied")
            input("please press enter to continue")
            exit(exit())
        #and here
        
        mainmenu = 0
        while mainmenu < 4:
            print("Menu:\n  1:  New password - register new password\n  2:  List - show passwords\n  3:  *UNDER CONSTRUCTION* Register new user - create another user account\n  4:  Exit")
            mainmenu = int(input("Enter a number:\n"))
            if mainmenu == 1:
                filea = open(nametest,"a")
                PassGen()
                cypher = codecs.encode(PassGen.password, 'ROT13')
                filea.write("\n" + cypher)
                filea.close()
                print("Done!")
            elif mainmenu == 2:
                filer = open(nametest,"r") #"a+" isn't reading the file
                contents = filer.read()
                plaintext = codecs.encode(contents, 'ROT13')
                print("Current Passwords: \n" + plaintext)
                filer.close()
            elif mainmenu == 3:
                print("New user registration is curently under construction.\n Menu:\n  1:  new password - register new password\n  2:  list - show passwords\n  4:  Exit")
                mainmenu = int(input("Enter a number:\n"))
            elif mainmenu == 4:
                exit(exit())
    elif login == 3:
        exit()