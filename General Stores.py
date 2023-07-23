cart = 0

bill = []

userInputItem = None
while userInputItem != "q":
    userInputItem = input("Enter item or press 'q' to quit : ")

    if (userInputItem == "maggie"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 15 * userInputQuantity
        bill.append(f"Maggie --- 15 --- {userInputQuantity} --- {userInputQuantity*15}")
    
    elif (userInputItem == "noodles"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Noodles --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
    
    elif (userInputItem == "pasta"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 40 * userInputQuantity
        bill.append(f"Pasta --- 40 --- {userInputQuantity} --- {userInputQuantity*40}")
    
    elif (userInputItem == "eggs"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 60 * userInputQuantity
        bill.append(f"Eggs --- 60 --- {userInputQuantity} --- {userInputQuantity*60}")
    
    elif (userInputItem == "bread"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 25 * userInputQuantity
        bill.append(f"Bread --- 25 --- {userInputQuantity} --- {userInputQuantity*25}")
    
    elif (userInputItem == "cheese"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 30 * userInputQuantity
        bill.append(f"Cheese --- 30 --- {userInputQuantity} --- {userInputQuantity*30}")
    
    elif (userInputItem == "tomato"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 30 * userInputQuantity
        bill.append(f"Tomato --- 30 --- {userInputQuantity} --- {userInputQuantity*30}")
    
    elif (userInputItem == "rice"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 50 * userInputQuantity
        bill.append(f"Rice --- 50 --- {userInputQuantity} --- {userInputQuantity*50}")
    
    elif (userInputItem == "popcorn"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Popcorn --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
    
    elif (userInputItem == "juice"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Juice --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
    
    elif (userInputItem == "coconut oil"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 40 * userInputQuantity
        bill.append(f"Coconut Oil --- 40 --- {userInputQuantity} --- {userInputQuantity*40}")
    
    elif (userInputItem == "butter"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 35 * userInputQuantity
        bill.append(f"Butter --- 35 --- {userInputQuantity} --- {userInputQuantity*35}")
    
    elif (userInputItem == "tea"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 10 * userInputQuantity
        bill.append(f"Tea --- 10 --- {userInputQuantity} --- {userInputQuantity*10}")

    elif (userInputItem == "coffee"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Coffee --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
    
    elif (userInputItem == "biscuit"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Biscuit --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
    
    elif (userInputItem == "milk"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 56 * userInputQuantity
        bill.append(f"Milk --- 56 --- {userInputQuantity} --- {userInputQuantity*56}")
    
    elif (userInputItem == "yoghurt"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 30 * userInputQuantity
        bill.append(f"Yoghurt --- 30 --- {userInputQuantity} --- {userInputQuantity*30}")
    
    elif (userInputItem == "curd"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Curd --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
    
    elif (userInputItem == "masala"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Masala --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
        
    elif (userInputItem == "salt"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Salt --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
        
    elif (userInputItem == "sugar"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 40 * userInputQuantity
        bill.append(f"Sugar --- 40 --- {userInputQuantity} --- {userInputQuantity*40}")
    
    elif (userInputItem == "water"):
        userInputQuantity = int(input("Enter quantity : "))
        cart = cart + 20 * userInputQuantity
        bill.append(f"Water --- 20 --- {userInputQuantity} --- {userInputQuantity*20}")
    
print()
for i in bill:
    print(i)
print(f"Your bill total is {cart}. Thanks for shopping with us.")


# ITEMS IN STORES
# MAGGIE         ==    ₹15
# NOODLES        ==    ₹20
# PASTA          ==    ₹40
# EGGS           ==    ₹60
# BREAD          ==    ₹25
# CHEESE         ==    ₹30
# TOMATO         ==    ₹30
# RICE           ==    ₹50
# POPCORN        ==    ₹20
# JUICE          ==    ₹20
# COCONUT OIL    ==    ₹40
# BUTTER         ==    ₹35
# TEA            ==    ₹10
# COFFEE         ==    ₹20
# BISCUIT        ==    ₹20
# MILK           ==    ₹56
# YOGHURT        ==    ₹30
# CURD           ==    ₹20
# MASALA         ==    ₹20
# SALT           ==    ₹20
# SUGAR          ==    ₹40
# WATER          ==    ₹20