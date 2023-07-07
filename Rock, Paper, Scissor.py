import random


def check(comp, user):
    if (comp == user):
        return 0
    if (comp == 1 and user == 3):
        return -1
    if (comp == 2 and user == 1):
        return -1
    if (comp == 3 and user == 2):
        return -1

    return 1


comp = random.randint(1,3)
user = int(input("1 for Rock, 2 for Paper, 3 for Scissor\n"))

score = check(comp, user)

# User's Choice
if user == 1:
    print("You : Rock")
elif user == 2:
    print("You : Paper")
elif user == 3:
    print("You : Scissor")
else:
    raise ValueError()

# Computer's Choice
if comp == 1:
    print("Computer : Rock\n")
elif comp == 2:
    print("Computer : Paper\n")
elif comp == 3:
    print("Computer : Scissor\n")
else:
    raise ValueError()

if (score == 0):
    print("It's a Draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")
