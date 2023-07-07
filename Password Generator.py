import string
import random

a = "".join(random.choice(string.ascii_lowercase)for i in range(10))
b = "".join(random.choice(string.ascii_uppercase)for i in range(10))
c = "".join(random.choice(string.digits)for i in range(10))
d = "".join(random.choice(string.punctuation)for i in range(10))

randomChoice = a+b+c+d

passwordlength = int(input("Enter password length : "))

password = "".join(random.choice(randomChoice)for i in range (passwordlength))
print(password)