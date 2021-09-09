import string
import random

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

PassGen()
print(PassGen.password)
