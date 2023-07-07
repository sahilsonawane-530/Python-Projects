num = int(input("Enter any number : "))
tableRange = int(input("Enter range : "))

for i in range(1, tableRange+1):
    print(f"{num} x {i} = {num*i}")