#Fibonacci Sequence Using Recursion
def Fibonacci(n):
    if n<=1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
user_input=int(input("Enter the nth term of the Fibonacci Series: "))
print(f"The Fibonacci Series till {user_input} term is:", end=" ")
for i in range(user_input):
    print(Fibonacci(i), end=" ")