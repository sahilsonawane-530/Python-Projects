import random

# Probability = Element Weight / Sum of All Weights

biasedSimulator = input("Want to roll the dice biasly (y/n) : ")

lst = [1,2,3,4,5,6]

if (biasedSimulator == "y"):
    biasedTowards = int(input("Biased towards : "))
    while True:
        if (biasedTowards == 1):
            print(random.choices(lst, weights=(100,20,15,12,10,5)))
        if (biasedTowards == 2):
            print(random.choices(lst, weights=(20,100,15,12,10,5)))
        if (biasedTowards == 3):
            print(random.choices(lst, weights=(10,5,100,20,15,12)))
        if (biasedTowards == 4):
            print(random.choices(lst, weights=(12,10,5,100,20,15)))
        if (biasedTowards == 5):
            print(random.choices(lst, weights=(15,12,10,5,100,20)))
        if (biasedTowards == 6):
            print(random.choices(lst, weights=(20,15,12,10,5,100)))
        anotherRoll = input("Want to roll again (y/n) : ")
        if (anotherRoll == "y"):
            continue
        else:
            break

else:
    while True:
        print(random.randint(1,6))
        anotherRoll = input("Want to roll again (y/n) : ")
        if (anotherRoll == "y"):
            continue
        else:
            break