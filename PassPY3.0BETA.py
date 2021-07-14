import codecs
import os
import os.path
import string
import random
from random import shuffle
import csv

DefaultSize = "mode con: cols=100 lines=20"  #fixes the size of the terminal window
os.system(DefaultSize)

account = ""
cypher = ""
username = ""
user_name = ""
r = ""

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

def PassGen(user_name,account,username):  #function to let the user create their own password or have one created for them
    x = 0
    while x < 3:
        x=int(input("1:  Have PassPY generate a password with a length you choose\n2:  Type your own password\n"))
        if x == 1:
            header()
            length = float(input("How many characters would you like the password to be?  \n"))
            div = int(length/3)  #there should be equal numbers of letters and numbers with the remainder going into punctuation
            r = int(length%3)
            seed = string.ascii_letters    # Generating letters
            letters = ( ''.  join(random.choice(seed) for i in range(div)) )

            seed = string.digits    # generating digits
            numbers = ( ''.join(random.choice(seed) for i in range(div)) )

            seed = string.punctuation    # generating punctuation
            punctuation = ( ''.join(random.choice(seed) for i in range(div + r)) )

            hold = letters + numbers + punctuation
            PassGen.password = ( ''.join(random.sample(hold, len(hold))))  #this will shuffle all of the letters, numbers and punctuation
            account = codecs.encode(account, 'ROT13')  #why not encrypt the account name and username as well as the password
            username = codecs.encode(username, 'ROT13')
            PassGen.password = codecs.encode(PassGen.password, 'ROT13')
            newline = account + "," + username + "," + PassGen.password
            with open(user_name + "passwords" + ".csv", "a", newline="\n") as filea:   #open the password storage file and write the new entry to it
                filea.write(newline + "\n")
            print("here is the generated password:  " + codecs.encode(PassGen.password, 'ROT13'))
            input("press Enter once the password is memorized (dont worry if you forget, it was saved in your password directory.)\n")
            MainMenu(user_name)   #go back to the main menu function
        elif x == 2:  #user created password
            header()
            PassGen.password = input("Type the password, then press Enter: \n")
            account = codecs.encode(account, 'ROT13')
            username = codecs.encode(username, 'ROT13')
            PassGen.password = codecs.encode(PassGen.password, 'ROT13')
            newline = account + "," + username + "," + PassGen.password
            with open(user_name + "passwords" + ".csv", "a", newline="\n") as filea:
                filea.write(newline + "\n")
            input("Press Enter...")
            MainMenu(user_name)
        else:
            Signin()  #go to the sign in function (Beginning)

def Signin():
    header()
    user_name = input("Enter Username: ")
    nametest2 = user_name + "login" + ".txt"
    try:
        usersearch = open(nametest2,"r")  #search for user's password file and if it exists prompt for the password
        lst = list(usersearch.readlines())
        confirm = lst[-1]
        print("Hello " + user_name)
        password = input("Enter Password: ")
        compare = codecs.encode(password, 'ROT13')
        if compare == confirm:
            print("Access Granted")
            nametest3 = user_name + "passwords" + ".txt"
            MainMenu(user_name)
        else:
            print("Access Denied")   #force exit if the password is wrong
            exit(exit())
    except FileNotFoundError:
        header()
        print("Access Denied")   #Force exit if the username does not exist
        input("please press enter to continue")
        exit(exit())

def AddEntry(user_name):  #function to add entry to password list
    header()
    filea = open(user_name + "passwords" + ".csv","a")
    account = input("what account is this password for? (e.g. GitHub)\n")
    username = input("What is the username for " + account + "?\n")
    PassGen(user_name,account,username)
    print("Done!")

def PasswordSearch(user_name):   #Password search function
    SearchColumn = int(input("Press 1 to show all passwords\nPress 2 to search by account\nPress 3 to search by username\nPress 4 to search by password\nPress 5 to return to the Main Menu\n   "))
    with open(user_name + "passwords" + ".csv") as csv_file:   #open the password file
        csv_reader = csv.reader(csv_file)   #opne in read mode
        if SearchColumn == 1:
            for row in csv_reader:    #iterate through the file and display all of the passwords then return to the main menu
                print(codecs.encode(row[2], 'ROT13'))
            r = input("Press Enter to continue to the Main Menu")
            MainMenu(user_name)
        elif SearchColumn == 2:
            search = input("What account are you looking for?  ")
            for row in csv_reader:   #iterate through the password file and compare the requested account with stored accounts, finally return any matches or return to the main menu
                if search == codecs.encode(row[0], 'ROT13'):
                    r = input(codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13'))
                    MainMenu(user_name)
        elif SearchColumn == 3:
            search = input("What username are you looking for?  ")   
            for row in csv_reader:   #iterate through the password file and compare the requested username with stored usernames, finally return any matches or return to the main menu
                if search == codecs.encode(row[1], 'ROT13'):
                    r = input(codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13'))
                    MainMenu(user_name)
        elif SearchColumn == 4:
            search = input("What password are you looking for?  ")
            for row in csv_reader:  #iterate through the password file and compare the requested password with stored passwords, finally return any matches or return to the main menu
                if search == codecs.encode(row[2], 'ROT13'):
                    r = input(codecs.encode(row[0], 'ROT13') + "     " + codecs.encode(row[1], 'ROT13') + "     " + codecs.encode(row[2], 'ROT13'))
                    MainMenu(user_name)
        elif SearchColumn == 5:
            MainMenu()
        else:
            Print("enter 1, 2, 3 or 4:\n")
    MainMenu(user_name)

def MainMenu(user_name):
    header()
    print("Menu:\n  1:  New password - register new password\n  2:  List - show passwords\n  3:  Exit")
    menu = int(input("Enter a number:\n"))
    if menu == 1:
        AddEntry(user_name)  #go to the add entry function
    elif menu == 2:
        PasswordSearch(user_name)  #go to the password search function
    elif menu == 3:
        clrscr()   #close the program
        exit()
    else:
        MainMenu()   #loop

def Register():
    header()
    NewUserLogin = input("Enter Username:  ")
    nametest1 = NewUserLogin + "login" + ".txt"
    try:
        usersearch = open(nametest1)  #search for user's password file and if it is already in use loop back to the beginning
        usersearch.close()
        header()
        print("User name not available")
        NewUserLogin = input("Press Enter to try again:  ")
        Register()
    except FileNotFoundError:  #if the fiel does not exist one wil be created
        header()
        print("User name is available")
    create = open(nametest1,"a")  #create user's password file
    #password = input("Enter password:  ")
    password1 = input("enter desired password:")
    cypher = codecs.encode(password1, 'ROT13')  #Encode the password
    create.write(cypher)
    create.close()
    print("Done!  New account created!\nWelcome.")



def Login():
    header()
    print("Welcome!\n 1:  New users - register your account\n 2:  Existing users - log in\n 3:  Exit - close the application.")
    login = int(input("Enter a number:\n"))
    if login == 1:
        Register()  #go to the registration function
    elif login == 2:
        Signin()  #go to the signin function
    elif login == 3:
        clrscr()  #exit the application
        exit()
    else:
        Login()  #Loop back to the beginning of this function

#Start the actual program
header()
print("Welcome to PassPY, the python based, opensource password storage\nIf you like PassPY, share it with a friend github.com/kayakers6/passpy\nIf you love PassPY, BTC:  bc1qsqc3v2jt3lh0kq9addf4gu6e2uq5vxxfk35pl\n                    SNX:  0x05E8813B7dc3c4e039D898CB13f21A6E4d675bc1")
start = input("Press ENTER to start")
Login()
