import os
import os.path
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.modes import CTR

account = "github.com"
userName = "/kayakers6"
password = "/PassPY"

string = account + userName + password
key = hashlib.sha256(string.encode('utf-8')) #.digest()

result = key.digest()


anum = key.hexdigest()
print(key)
print(result)
print(len(result))
print(anum)
print(len(anum))

iv = bytes(int(len(result)/2))

print(iv)
# arr = bytes(key, 'utf-8')
# print(arr)
# print(len(arr))

cipher = Cipher(algorithms.AES(result), modes.CTR(iv))

encryptor = cipher.encryptor()
un = encryptor.update(b"Boss") + encryptor.finalize()
print(un)

encryptor = cipher.encryptor()

acc = encryptor.update(b"PassPY") + encryptor.finalize()
print(acc)

encryptor = cipher.encryptor()

pw = encryptor.update(b"Password") + encryptor.finalize()
print(pw)

concat = acc + un + pw

print(concat)

checksum = hashlib.sha256(concat)
print(checksum)
hexi = checksum.hexdigest()
print(hexi)

with open("password.csv","a") as file:
    file.write(str(acc) + "\t" + str(un) + "\t" + str(pw) + "\t" + str(anum) + "\t" + str(hexi) + "\n")

filecheck = hashlib.sha256("password.csv")


cipher = Cipher(algorithms.AES(filecheck), modes.CTR(iv))
print("Done")