import codecs
import socket
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 8080
s.bind((socket.gethostname(), 8080))
s.listen(5)
print(host)
print("waiting for incoming connections... ")
conn, addr = s.accept()
print(addr, "Has connected to the server")
dataTest = ""
while True:
    # accept connections from outside
    # clientsocket lets you send/receive data from the client
    # address is a tuple that contains the client IP and port
    (clientsocket, address) = s.accept()
    # now do something with the clientsocket
    # in this case we'll receive 1024 bytes of data, then print it
    data = clientsocket.recv(3000)
    print(data)
    # then send the data back (called an echo server)
    clientsocket.send("response")
    data2 = conn.recv(1024)
    decoded = print(data2.decode())
    
    if decoded == "2":
        Signin()
    elif decoded == "1":
        RegisterAcct()

    def Signin():
        user_name = decoded
        nametest2 = user_name + "login" + ".txt"
        try:
            usersearch = open(nametest2,"r")  #search for user's password file and if it exists prompt for the password
            lst = list(usersearch.readlines())
            confirm = lst[-1]
            password = input("problem")
            compare = codecs.encode(decoded, 'ROT13')
            if compare == confirm:
                clientsocket.send("access granted! welcome back!")
            else:
                clientsocket.send("Access Denied")
                s.close
        except FileNotFoundError:
            clientsocket.send("Access Denied")
            s.close

    def RegisterAcct():
        NewUserLogin = decoded
        nametest1 = NewUserLogin + "login" + ".txt"
        try:
            usersearch = open(nametest1)  #search for user's password file and if it is already in use loop back to the beginning
            usersearch.close()
            clientsocket.send("User name not available")
            NewUserLogin = input("Press Enter to try again:  ")
            RegisterAcct()
        except FileNotFoundError:  #if the fiel does not exist one wil be created
            clientsocket.send("User name is available")
        create = open(nametest1,"a")  #create user's password file
        #password = input("Enter password:  ")
        password1 = decoded
        cypher = codecs.encode(password1, 'ROT13')  #Encode the password
        create.write(cypher)
        create.close()
        clientsocket.send("Done!  New account created!\nWelcome.")