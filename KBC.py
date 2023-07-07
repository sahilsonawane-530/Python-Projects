name = str(input("Enter your name : "))
print("Hello,", name)

q1 = "\nWhen did India got it's independence?"
q2 = "\nWhich of the following corresponds to 'ek bataa do'?"
q3 = "\nWhich of the following deities is also known as 'Gauri Nandan'?"
q4 = "\nIn the game of ludo the discs or tokens are of how many colours?"
q5 = "\nWhich of these national parks are located in Madhya Pradesh?"
q6 = "\nWhere was BRICS summit held in 2014?"
q7 = "\nWhich of these terms can only be used for women?"
q8 = "\nThe wife of which of these famous sports persons was once captain of Indian volleyball team?"
q9 = "\nWho wrote the introduction to the English translation of Rabindranath Tagore's Gitanjali?"
q10 = "\nWhich day is celebrated as Sports Day every year?"

l1 = ("1950", "1964", "1947", "1945")
l2 = ("Pura", "Sava", "Adha", "Pauna")
l3 = ("Agni", "Indra", "Hanuman", "Ganesha")
l4 = ("One", "Two", "Three", "Four")
l5 = ("Krishna & Kanhaiya", "Kanha & Madhav", "Ghanshyam & Murari", "Girdhar & Gopal")
l6 = ("Brazil", "India", "Russia", "South Africa")
l7 = ("Dirghaayu", "Suhagan", "Chiranjeevi", "Sushil")
l8 = ("K.D.Jadhav", "Dhyan Chand", "Prakash Padukone", "Milkha Singh")
l9 = ("PB Shelly", "Alred Tennyson", "WB Yeats", "TS Elliot")
l10 = ("29 August", "2nd October", "26th July", "22nd April")

ans1 = None
ans2 = None
ans3 = None
ans4 = None
ans5 = None
ans6 = None
ans7 = None
ans8 = None
ans9 = None
ans10 = None
moneyWon = 0

print(q1)
print(l1)

ans1 = int(input("Please enter your answer : "))

if (ans1 == 1):
    print("Sorry, you loose!")
elif (ans1 == 2):
    print("Sorry, you loose!")
elif (ans1 == 3):
    print("Congratulations, you won ₹10,000/-")
    moneyWon = 10000
elif (ans1 == 4):
    print("Sorry, you loose!")
else:
    print(ans1)

if (ans1 == 3):
    print(q2, "Your options are")
    print(l2)

    ans2 = int(input("Please enter your answer : "))

    if (ans2 == 1):
        print("Sorry, you loose!")
    elif (ans2 == 2):
        print("Sorry, you loose!")
    elif (ans2 == 3):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 20000
    elif (ans2 == 4):
        print("Sorry, you loose!")
    else:
    	print(ans2)

if (ans2 == 3):
    print(q3, "Your options are")
    print(l3)

    ans3 = int(input("Please enter your answer : "))

    if (ans3 == 1):
        print("Sorry, you loose!")
    elif (ans3 == 2):
        print("Sorry, you loose!")
    elif (ans3 == 3):
        print("Sorry, you loose!")
    elif (ans3 == 4):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 30000
    else:
    	print(ans3)

if (ans3 == 4):
    print(q4, "Your options are")
    print(l4)

    ans4 = int(input("Please enter your answer : "))

    if (ans4 == 1):
        print("Sorry, you loose!")
    elif (ans4 == 2):
        print("Sorry, you loose!")
    elif (ans4 == 3):
        print("Sorry, you loose!")
    elif (ans4 == 4):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 40000
    else:print(ans4)

if (ans4 == 4):
    print(q5, "Your options are")
    print(l5)

    ans5 = int(input("Please enter your answer : "))

    if (ans5 == 1):
        print("Sorry, you loose!")
    elif (ans5 == 2):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 50000
    elif (ans5 == 3):
        print("Sorry, you loose!")
    elif (ans5 == 4):
        print("Sorry, you loose!")
    else:
        print(ans5)

if (ans5 == 2):
    print(q6, "Your options are")
    print(l6)

    ans6 = int(input("Please enter your answer : "))

    if (ans6 == 1):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 60000
    elif (ans6 == 2):
        print("Sorry, you loose!")
    elif (ans6 == 3):
        print("Sorry, you loose!")
    elif (ans6 == 4):
        print("Sorry, you loose!")
    else:
        print(ans6)

if (ans6 == 1):
    print(q7, "Your options are")
    print(l7)

    ans7 = int(input("Please enter your answer : "))

    if (ans7 == 1):
        print("Sorry, you loose!")
    elif (ans7 == 2):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 70000
    elif (ans7 == 3):
        print("Sorry, you loose!")
    elif (ans7 == 4):
        print("Sorry, you loose!")
    else:
        print(ans7)

if (ans7 == 2):
    print(q8, "Your options are")
    print(l8)

    ans8 = int(input("Please enter your answer : "))

    if (ans8 == 1):
        print("Sorry, you loose!")
    elif (ans8 == 2):
        print("Sorry, you loose!")
    elif (ans8 == 3):
        print("Sorry, you loose!")
    elif (ans8 == 4):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 80000
    else:
        print(ans8)

if (ans8 == 4):
    print(q9, "Your options are")
    print(l9)

    ans9 = int(input("Please enter your answer : "))

    if (ans9 == 1):
        print("Sorry, you loose!")
    elif (ans9 == 2):
        print("Sorry, you loose!")
    elif (ans9 == 3):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 90000
    elif (ans9 == 4):
        print("Sorry, you loose!")
    else:
        print(ans9)

if (ans9 == 3):
    print(q10, "Your options are")
    print(l10)

    ans10 = int(input("Please enter your answer : "))

    if (ans10 == 1):
        print("Congratulations, you won ₹10,000/-")
        moneyWon = 100000
    elif (ans10 == 2):
        print("Sorry, you loose!")
    elif (ans10 == 3):
        print("Sorry, you loose!")
    elif (ans10 == 4):
        print("Sorry, you loose!")
    else:
        print(ans10)

print("\nYou can take ₹", moneyWon,"to your home")