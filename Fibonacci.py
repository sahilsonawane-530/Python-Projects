def fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1 or n == 2):
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input("Enter number : "))))

# f0=0
# f1=1
# f2=f1+fo

# f20=f19+f18
# 0 1 1 2 3 5 8 13 21 34 55 89