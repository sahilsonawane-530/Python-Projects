import random

randInt1 = random.randint(10,50)
randInt2 = random.randint(10,50)
randInt3 = random.randint(10,50)
randInt4 = random.randint(10,50)
randInt5 = random.randint(10,50)
randInt6 = random.randint(10,50)
randInt7 = random.randint(10,50)

userNumber = int(input("Enter any number : "))

str1 = str(input(f"Add {randInt1} to your choosed number (y/n) : "))

if (str1 == "y"):
    str2 = str(input(f"Less {randInt2} : "))
    if (str2 == "y"):
        str3 = str(input(f"Add {randInt3} : "))
        if (str3 == "y"):
            str4 = str(input("Less your choosed number : "))
            if (str4 == "y"):
                str5 = str(input(f"Multiply by {randInt4} : "))
                if (str5 == "y"):
                    str6 = str(input(f"Less {randInt5} : "))
                    if (str6 == "y"):
                        str7 = str(input(f"Add {randInt6} : "))
                        if (str7 == "y"):
                            str8 = str(input(f"Less {randInt7} : "))
else:
    print(f"\nYour choosed number was : {userNumber}")

print(f"\nYour choosed number was : {userNumber}")
print(f"Number you got is : {(((((randInt1-randInt2)+randInt3)*randInt4)-randInt5)+randInt6)-randInt7}")