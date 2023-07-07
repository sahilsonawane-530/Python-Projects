# Factorial(7) = 7*6*5*4*3*2*1
# Factorial(6) = 6*5*4*3*2*1
# Factorial(5) = 5*4*3*2*1
# Factorial(4) = 4*3*2*1
# Factorial(3) = 3*2*1
# Factorial(2) = 2*1
# Factorial(1) = 1
# Factorial(0) = 1

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Enter number : "))))

# THIS IS HOW FACTORIAL FUNCTION WORKS
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)