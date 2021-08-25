import os
import os.path
import struct
import hashlib
import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.modes import CTR

account = input("what is the name of the account you want to encrypt? \n")
userName = input("What is the username of the account you want to encrypt?  \n")
password = input("What is the password for the account you want to encrypt?  \n")

preKey = account + userName + password
lineHash = hashlib.sha256(preKey.encode('utf-8'))

key = lineHash.digest()

lineHashHexidecimal = lineHash.hexdigest()

iv = bytes(int(len(key)/2))

bacc = bytes(account, 'utf8')
bun = bytes(userName, 'utf8')
bpas = bytes(password, 'utf8')

cipher = Cipher(algorithms.AES(key), modes.CTR(iv))

encryptor = cipher.encryptor()
un = encryptor.update(bun) + encryptor.finalize()

encryptor = cipher.encryptor()
acc = encryptor.update(bacc) + encryptor.finalize()

encryptor = cipher.encryptor()
pw = encryptor.update(bpas) + encryptor.finalize()

lineEncrypted = acc + un + pw

lineChecksum = hashlib.sha256(lineEncrypted).hexdigest()

with open("apassword.csv","a") as file:
    file.write(str(acc) + "\t" + str(un) + "\t" + str(pw) + "\t" + str(lineHashHexidecimal) + "\t" + str(lineChecksum) + "\n")

h = hashlib.sha256()
with open("apassword.csv", "rb")as file:
    while True:
        chunk = file.read(h.block_size)
        if not chunk:
            break
        h.update(chunk)

fileHexidecimal = h.hexdigest()
fileKey = h.digest()

iv = bytes(int(len(fileKey)/2))

with open("acksum.txt", "w") as file:
    file.write(str(fileHexidecimal + "\n"))

cipher = Cipher(algorithms.AES(fileKey), modes.CTR(iv))
encryptor = cipher.encryptor()

fileSize = os.path.getsize("apassword.csv")

with open("apassword.csv", "rb") as fileR:
    content = fileR.read()
    scrambled = encryptor.update(content) + encryptor.finalize()
with open("aEpassword.csv", "wb")as fileE:
    fileE.write(scrambled)

h = hashlib.sha256()
with open("aEpassword.csv", "rb")as file:
    while True:
        chunk = file.read(h.block_size)
        if not chunk:
            break
        h.update(chunk)

fileHexidecimal = h.hexdigest()

with open("acksum.txt", "a") as file:
    file.write(str(fileHexidecimal + "\n"))


print("Done")
