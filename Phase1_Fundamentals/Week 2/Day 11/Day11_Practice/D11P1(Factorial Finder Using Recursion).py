#Factorial Finder Using Recursion
def get_factorial(n):
    if n<2:
        return 1
    else:
        return n*get_factorial(n-1)
user_input=int(input("Enter the number to know its Factorial: "))
Factorial=get_factorial(user_input)
print(f"{user_input}! is: {Factorial}")