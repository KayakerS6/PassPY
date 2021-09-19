import codecs
import os
import os.path
import string
import random
from random import shuffle
import csv
import time
import hashlib
import struct
import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

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

def PassGen(user_name,acc,uN,pre):
    header()
    x = ''
    x = input("1:  Have PassPY generate a password with a length you choose for " + acc + "\n2:  Type your own password for " + acc + "\n")
    if x == '1':
        header()
        length = float(input("How many characters would you like the password to be for " + acc + "?  \n"))
        div = int(length/3)
        r = int(length%3)
        seed = string.ascii_letters    # Generating letters
        letters = ( ''.  join(random.choice(seed) for i in range(div)) )

        seed = string.digits    # generating digits
        numbers = ( ''.join(random.choice(seed) for i in range(div)) )

        seed = string.punctuation    # generating punctuation
        punctuation = ( ''.join(random.choice(seed) for i in range(div + r)) )

        hold = letters + numbers + punctuation
        pW = ( ''.join(random.sample(hold, len(hold))))
        print("here is the generated password:  " + pW)
        preKey = acc + uN + pW
        lineHash = hashlib.sha256(preKey.encode('utf-8'))
        
        half = hashlib.sha256(user_name.encode('utf-8')).hexdigest()

        lineHashHexidecimal = lineHash.hexdigest()            

        smosh = hashlib.sha256(bytes(half + lineHashHexidecimal, 'utf8'))
        
        key = smosh.digest()

        iv = bytes(int(len(key)/2))

        acc = bytes(acc, 'utf8')
        uN = bytes(uN, 'utf8')
        pW = bytes(pW, 'utf8')

        cipher = Cipher(algorithms.AES(key), modes.CTR(iv))

        encryptor = cipher.encryptor()
        uN = encryptor.update(uN) + encryptor.finalize()
        uN = bytes.hex(uN)

        encryptor = cipher.encryptor()
        acc = encryptor.update(acc) + encryptor.finalize()
        acc = bytes.hex(acc)

        encryptor = cipher.encryptor()
        pW = encryptor.update(pW) + encryptor.finalize()
        pW = bytes.hex(pW)

        lineEncrypted = bytes(acc + uN + pW, 'utf8')

        lineChecksum = hashlib.sha256(lineEncrypted).hexdigest()
        newline = acc + "\t" + uN + "\t" + pW + "\t" + str(lineHashHexidecimal) + "\t" + str(lineChecksum) + "\n"
        post = user_name + "passwords" + ".passpy"
        location = os.path.join(pre, post)
        with open(location, "a", newline="\n") as filea:
            filea.write(newline + "\n")

        input("press Enter once the password is memorized (dont worry if you forget, it was saved in your password directory.)\n")
        MainMenu(user_name)
    elif x == '2':
        header()
        pW = input("Type the password for " + acc + ", then press Enter: \n")
        preKey = acc + uN + pW
        lineHash = hashlib.sha256(preKey.encode('utf-8'))
        half = hashlib.sha256(user_name.encode('utf-8')).hexdigest()

        lineHashHexidecimal = lineHash.hexdigest()            

        smosh = hashlib.sha256(bytes(half + lineHashHexidecimal, 'utf8'))
        
        key = smosh.digest()

        iv = bytes(int(len(key)/2))

        acc = bytes(acc, 'utf8')
        uN = bytes(uN, 'utf8')
        pW = bytes(pW, 'utf8')

        cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
        
        smosh = ''
        key = ''
        iv = ''
        
        encryptor = cipher.encryptor()
        uN = encryptor.update(uN) + encryptor.finalize()
        uN = bytes.hex(uN)

        encryptor = cipher.encryptor()
        acc = encryptor.update(acc) + encryptor.finalize()
        acc = bytes.hex(acc)

        encryptor = cipher.encryptor()
        pW = encryptor.update(pW) + encryptor.finalize()
        pW = bytes.hex(pW)

        lineEncrypted = bytes(acc + uN + pW, 'utf8')

        lineChecksum = hashlib.sha256(lineEncrypted).hexdigest()
        newline = acc + "\t" + uN + "\t" + pW + "\t" + str(lineHashHexidecimal) + "\t" + str(lineChecksum) + "\n"
        post = user_name + "passwords" + ".passpy"
        location = os.path.join(pre, post)
        with open(location, "a", newline="\n") as filea:
            filea.write(newline)
        MainMenu(user_name)
    else:
        PassGen(user_name,acc,uN,pre)

def Signin(pre):
    header()
    user_name = input("Enter Username: ").encode("utf-8").hex()
    nametest2 = user_name + "login" + ".passpy"
    location = os.path.join(pre, nametest2)
    try:     #check to see if the account exists
        usersearch = open(location,"r")  #search for user's password file
        lst = list(usersearch.readlines())
        confirm = lst[-1]
        print("Hello " + str(codecs.decode(user_name, "hex"), "utf-8"))
        password = input("Enter Password: ").encode("utf-8").hex()
        s(user_name,password)
        compare = line
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
    acc = input("what account is this password for? (e.g. GitHub)\n")
    uN = input("What is the username for " + acc + "?\n")
    PassGen(user_name,acc,uN,pre)

    print("Done!")

def PasswordSearch(user_name,pre):
    c = ""
    header()
    post = user_name + "passwords" + ".passpy"
    location = os.path.join(pre, post)
    half = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
    SearchColumn = input("Password Search Menu:\nPress 1 to show all passwords\nPress 2 to search by account\nAll of the following options will NOT work!\nPress 3 to search by username\nPress 4 to search by password\nPress 5 to return to the Main Menu\n   ")
    try:     #make sure there is a password file to search through
        with open(location) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            if SearchColumn == '1':  
                # header()
                print("Here are all of the stored passwords:  ")
                for row in csv_reader: # !!!START HERE!!! Decrypt single item line by line
                    smosh = hashlib.sha256(bytes(half + str(row[3]), 'utf8'))
                    key = smosh.digest()
                    iv = bytes(int(len(key)/2))
                    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
                    decryptor = cipher.decryptor()
                    bEntry = bytes.fromhex(str(row[2]).lower())
                    bct = str(decryptor.update(bEntry), "utf8")
                    print(bct)
                input("Press Enter to continue to the Main Menu")
                MainMenu(user_name)
            elif SearchColumn == '2':
                header()
                search = bytes(input("What Account are you looking for?  \n"), 'utf8')
                for row in csv_reader:
                    half = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
                    smosh = hashlib.sha256(bytes(half + str(row[3]), 'utf8'))
                    key = smosh.digest()
                    iv = bytes(int(len(key)/2))
                    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
                    decryptor = cipher.decryptor()
                    encryptor = cipher.encryptor()
                    sup = encryptor.update(search) + encryptor.finalize()
                    sable = bytes.hex(sup)
                    if sable == row[0]:
                        decryptor = cipher.decryptor()
                        a = bytes.fromhex(str(row[0]).lower())
                        a = str(decryptor.update(a), "utf8")
                        decryptor = cipher.decryptor()
                        u = bytes.fromhex(str(row[1]).lower())
                        u = str(decryptor.update(u), "utf8")
                        decryptor = cipher.decryptor()
                        p = bytes.fromhex(str(row[2]).lower())
                        p = str(decryptor.update(p), "utf8")
                        header()
                        c = input("The Account, Username and Password information for " + a + " are:\n" + a + "     " + u + "     " + p + "\nEnter 1 if you want to copy the password to the clipboard\nEnter 2 if you do not\n")
                        if c == '1':
                            target = p
                            header()
                            print("The Account, Username and Password information for " + a + " are:\n" + a + "     " + u + "     " + p)
                            Clipboard(target)
                            MainMenu(user_name)
                        elif c == '2':
                            input("Password NOT copied, Press enter to continue looking")
                            continue
                        else:
                            input("Password NOT copied, Press enter to return to the Main Menu")
                            MainMenu(user_name)
                MainMenu(user_name)
            elif SearchColumn == '3':
                header()
                search = bytes(input("What Username are you looking for?  \n"), 'utf8')
                for row in csv_reader:
                    half = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
                    smosh = hashlib.sha256(bytes(half + str(row[3]), 'utf8'))
                    key = smosh.digest()
                    iv = bytes(int(len(key)/2))
                    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
                    decryptor = cipher.decryptor()
                    encryptor = cipher.encryptor()
                    sup = encryptor.update(search) + encryptor.finalize()
                    sable = bytes.hex(sup)
                    if sable == row[1]:
                        decryptor = cipher.decryptor()
                        a = bytes.fromhex(str(row[0]).lower())
                        a = str(decryptor.update(a), "utf8")
                        decryptor = cipher.decryptor()
                        u = bytes.fromhex(str(row[1]).lower())
                        u = str(decryptor.update(u), "utf8")
                        decryptor = cipher.decryptor()
                        p = bytes.fromhex(str(row[2]).lower())
                        p = str(decryptor.update(p), "utf8")
                        header()
                        c = input("The Account, Username and Password information for " + a + " are:\n" + a + "     " + u + "     " + p + "\nEnter 1 if you want to copy the password to the clipboard\nEnter 2 if you do not\n")
                        if c == '1':
                            target = p
                            header()
                            print("The Account, Username and Password information for " + a + " are:\n" + a + "     " + u + "     " + p)
                            Clipboard(target)
                            MainMenu(user_name)
                        elif c == '2':
                            input("Password NOT copied, Press enter to return to continue searching")
                            continue
                        else:
                            input("Password NOT copied, Press enter to return to the Main Menu")
                            MainMenu(user_name)
                    continue
                    MainMenu(user_name)
            elif SearchColumn == '4':
                header()
                search = bytes(input("What password are you looking for?  \n"), 'utf8')
                for row in csv_reader:
                    half = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
                    smosh = hashlib.sha256(bytes(half + str(row[3]), 'utf8'))
                    key = smosh.digest()
                    iv = bytes(int(len(key)/2))
                    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
                    decryptor = cipher.decryptor()
                    encryptor = cipher.encryptor()
                    sup = encryptor.update(search) + encryptor.finalize()
                    sable = bytes.hex(sup)
                    if sable == row[2]:
                        decryptor = cipher.decryptor()
                        a = bytes.fromhex(str(row[0]).lower())
                        a = str(decryptor.update(a), "utf8")
                        decryptor = cipher.decryptor()
                        u = bytes.fromhex(str(row[1]).lower())
                        u = str(decryptor.update(u), "utf8")
                        decryptor = cipher.decryptor()
                        p = bytes.fromhex(str(row[2]).lower())
                        p = str(decryptor.update(p), "utf8")
                        header()
                        c = input("The Account, Username and Password information for " + a + " are:\n" + a + "     " + u + "     " + p + "\nEnter 1 if you want to copy the password to the clipboard\nEnter 2 if you do not\n")
                        if c == '1':
                            target = p
                            header()
                            print("The Account, Username and Password information for " + a + " are:\n" + a + "     " + u + "     " + p)
                            Clipboard(target)
                            MainMenu(user_name)
                        elif c == '2':
                            input("Password NOT copied, Press enter to return to continue")
                            continue
                        else:
                            input("Password NOT copied, Press enter to return to the Main Menu")
                            MainMenu(user_name)
                    continue
                    MainMenu(user_name)
            elif SearchColumn == '5':
                MainMenu(user_name)
            else:
                m = input("enter 1, 2, 3 or 4:\n")
                PasswordSearch(user_name,pre)
        MainMenu(user_name)
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
    menu = input("Enter a number:\n")
    if menu == '1':
        AddEntry(user_name,pre)
    elif menu == '2':
        PasswordSearch(user_name,pre)
    elif menu == '3':
        clrscr()
        exit()
    elif menu == '':
        MainMenu(user_name)
    else:
        MainMenu(user_name)

def s(user_name,password):
    uhold = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
    phold = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for i in uhold:
        if i.isdigit():
            ucount = i
            break
    for i in phold:
        if i.isdigit():
            pcount = i
            break
    global line 
    if int(pcount) % 2 == 0:
        line = uhold * int(pcount) + phold * int(ucount)
    else:
        line = phold * int(pcount) + uhold * int(pcount)
    line = hashlib.sha256(line.encode('utf-8')).hexdigest()

def Register(pre):
    header()
    user_name = input("Enter Username:  ").encode("utf-8").hex()
    nametest1 = user_name + "login" + ".passpy"
    location = os.path.join(pre, nametest1)
    try:
        usersearch = open(location)  #search for user's password file
        usersearch.close()
        header()
        print("User name not available")
        input("Press Enter to try again:  ")
        Register(pre)
    except FileNotFoundError:
        header()
        print("User name is available")
        create = open(location,"a")  #create user's password file
        password = input("enter desired password:\n").encode("utf-8").hex()
        s(user_name,password)
        create.write(line)
        create.close()
        header()
        input("Done!  \nNew account created!\nWelcome!")
        MainMenu(user_name)

def Login(pre):
    header()
    print("Welcome!\n 1:  New users - register your account\n 2:  Existing users - log in\n 3:  Exit - close the application.")
    login = input("Enter a number:\n")
    if login == '1':
        Register(pre)
    elif login == '2':
        Signin(pre)
    elif login == '3':
        clrscr()
        exit()
    else:
        Login(pre)

# Startup Phase
header()
print("Welcome to PassPY, the python based, opensource password storage\nIf you like PassPY, share it with a friend github.com/kayakers6/passpy\nIf you love PassPY, BTC:  bc1qsqc3v2jt3lh0kq9addf4gu6e2uq5vxxfk35pl\n                    SNX:  0x05E8813B7dc3c4e039D898CB13f21A6E4d675bc1")
start = input("Press ENTER to start")
Login(pre)
