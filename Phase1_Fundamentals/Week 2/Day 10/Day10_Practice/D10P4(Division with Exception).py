'''
Division with Exception:
Handle ZeroDivisionError when dividing two numbers.
'''
a=int(input("Enter the Dividend: "))
b=int(input("Enter the Divisor: "))
try:
    result=a/b
    print(f"{a} divided by {b} gives: {result}")
except ZeroDivisionError:
    print("You can't divide with zero!")