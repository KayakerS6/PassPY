import codecs
import os
import os.path
import csv

print("testing csv creation")
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
print("log new account")

create = open(nametest,"a")  #create user's password file
password = input("Enter password:  ")
#cypher = codecs.encode(password, 'ROT13')  #Change to sha  !plaintext is easier to read!
create.write(password)
create.close()
print("Done!  New account created!\nWelcome.")

accountlog = NewUser + ".csv"
familiar = input("what is an easy to remember name for this account?  ")
Username = input("what is the username for " + familiar + "?  ")
Password = input("what is the password for " + familiar + "?  ")

with open(accountlog, mode="a") as account:
    account_writer = csv.writer(account, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    account_writer.writerow([familiar, Username, Password])


#this is currently illetirate and will not print the lines of the file
secret = csv.reader(accountlog, newline='')
for row in secret:
    print(row)