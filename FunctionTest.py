import os
import os.path


NewUser = input("Enter Username:  ")
nametest = NewUser + ".txt"
accountlog = NewUser + ".csv"
FileFound = "Username not available"
FileNotFound = "Username is available"
def AccountSearch(nametest):
	try:
		usersearch = open(nametest)  #search for user's password file
		usersearch.close()
		print(FileFound)
	except FileNotFoundError:
		print(FileNotFound)

AccountSearch(nametest)
#start loop
if os.path.exists(nametest):
    NewUser = input("Enter Username:  ")
    nametest = NewUser + ".txt"
    accountlog = NewUser + ".csv"
    FileFound = "Username not available"
    FileNotFound = "Username is available"
    AccountSearch(nametest)
else:
    password = input("Enter password:  ")
    create = open(nametest,"w")
    create.write(password)
    create.close()