questions = [
    [
        "When did India got it's independence?",
        "1950", "1964", "1947", "1945", 3
    ],
    [
        "Which of the following corresponds to 'ek bataa do'?",
        "Pura", "Sava", "Adha", "Pauna", 3
    ],
    [
        "Which of the following deities is also known as 'Gauri Nandan'?",
        "Agni", "Indra", "Hanuman", "Ganesha", 4
    ],
    [
        "In the game of ludo the discs or tokens are of how many colours?",
        "One", "Two", "Three", "Four", 4
    ],
    [
        "Which of these national parks are located in Madhya Pradesh?",
        "Krishna & Kanhaiya", "Kanha & Madhav", "Ghanshyam & Murari", "Girdhar & Gopal", 2
    ],
    [
        "Where was BRICS summit held in 2014?",
        "Brazil", "India", "Russia", "South Africa", 1
    ],
    [
        "Which of these terms can only be used for women?",
        "Dirghaayu", "Suhagan", "Chiranjeevi", "Sushil", 2
    ],
    [
        "The wife of which of these famous sports persons was once captain of Indian volleyball team?",
        "K.D.Jadhav", "Dhyan Chand", "Prakash Padukone", "Milkha Singh", 4
    ],
    [
        "Who wrote the introduction to the English translation of Rabindranath Tagore's Gitanjali?",
        "PB Shelly", "Alred Tennyson", "WB Yeats", "TS Elliot", 3
    ],
    [
        "Which day is celebrated as Sports Day every year?",
        "29 August", "2nd October", "26th July", "22nd April", 1
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):

    print(f"Question for Rs. {levels[i]}")
    question = questions[i]
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit : "))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"You can take home Rs.{money}")