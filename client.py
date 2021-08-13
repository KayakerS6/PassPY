import socket
s = socket.socket()
host = '66.56.219.47'
port = 8080
s.connect((host, port))
print("connecting...")
while True:
    text = input("message:").encode()
    s.send(text)