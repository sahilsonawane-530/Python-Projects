import string
import random

def Encrypt():
    ''' extracts 1st letter and inserts it at the end, appends 6 letters at start and 6 letters at end, reveres's the string '''
    b = str(input("Enter message : "))
    words = b.split(" ")
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = r1 + r2 + word[1:] + r3 + word[0] + r4 + r5
            nwords.append(stnew)
        else:
            nwords.append(word)
    a = " ".join(nwords)
    print(reverseRecursion(a))

def Decrypt():
    ''' reverse's the string, extracts 6 letters from start & 6 letters from end, extracts last letter and inserts it at the start '''
    b = str(input("Enter message : "))
    b = reverseRecursion(b)
    words = b.split(" ")
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[6:-6]
            stnew = stnew[-1] + stnew[:-1]
            stnew = stnew[:-3]
            nwords.append(stnew)
        else:
            nwords.append(word)
    print(" ".join(nwords))

def reverseRecursion(x):
    ''' reversing '''
    if len(x) == 0:
        return x
    else:
        return reverseRecursion(x[1:]) + x[0]

a = int(input("Press 1 for Encrypting\nPress 2 for Decrypting\nPress 3 for Quitting\n"))
r1 = "".join((random.choice(string.ascii_lowercase)for x in range(3)))
r2 = "".join((random.choice(string.ascii_lowercase)for x in range(3)))
r3 = "".join((random.choice(string.ascii_lowercase)for x in range(3)))
r4 = "".join((random.choice(string.ascii_lowercase)for x in range(3)))
r5 = "".join((random.choice(string.ascii_lowercase)for x in range(3)))

if (a == 1):
    Encrypt()

elif (a == 2):
    Decrypt()

elif (a == 3):
    print("Thank you for quitting")
    exit()

else:
    raise ValueError()