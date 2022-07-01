# Random password generator that will generate a password with a length of 8 characters
# TODO: Expand on this so it can create a password of any lenght, minimum 8 characters
import random

password = [None] * 8

# generate 2 uppercase letters
password[0] = chr(random.randint(65,90))
password[1] = chr(random.randint(65,90))

# lowercase letters

password[2] = chr(random.randint(97,122))
password[3] = chr(random.randint(97,122))

# Digits

password[4] = chr(random.randint(48,57))
password[5] = chr(random.randint(48,57))

# Symbols
password[6] = chr(random.randint(33,95))
password[7] = chr(random.randint(33,95))

# Shuffle the password
random.shuffle(password)
for x in password:
    print(x, end='')

