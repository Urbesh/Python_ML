#Sum of Digits Using Recursion
def Sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + Sum_of_digits(n//10)
user_input=int(input("Enter the a number to know its Sum of digits: "))
result=Sum_of_digits(user_input)
print(f"The Sum of the Digits {user_input} is: {result}")