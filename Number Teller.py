num = int(input("Enter any number : "))

if(num<0):
    print("Your number is negavite")
elif(num>0):
    if(1<=num<=10):
        print("Your number is between 1 - 10")
    elif(11<=num<=20):
        print("Your number is between 11 - 20")
    elif(21<=num<=30):
        print("Your number is between 21 - 30")
    elif(31<=num<=40):
        print("Your number is between 31 - 40")
    elif(41<=num<=50):
        print("Your number is between 41 - 50")
    elif(51<=num<=60):
        print("Your number is between 51 - 60")
    elif(61<=num<=70):
        print("Your number is between 61 - 70")
    elif(71<=num<=80):
        print("Your number is between 71 - 80")
    elif(81<=num<=90):
        print("Your number is between 81 - 90")
    elif(91<=num<=100):
        print("Your number is between 91 - 100")
    else:
        print("Your number is greater than 100")
else:
    print("Your number is Zero")