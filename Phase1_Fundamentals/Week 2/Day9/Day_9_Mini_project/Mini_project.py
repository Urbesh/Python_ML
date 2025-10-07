"""
💡 Goal

Build a simple Lambda-based calculator that performs arithmetic operations using lambda expressions.

🧱 Features

Menu-driven calculator:

Add

Subtract

Multiply

Divide

Each operation implemented using a lambda.

Option to run multiple times.
"""
add=lambda a,b: a+b
sub=lambda a,b: a-b
mul=lambda a,b: a*b
div=lambda a,b: a/b if b!=0 else "Error! Division by Zero"
while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    user_input=int(input("Enter Choice: "))
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    if user_input==1:
        print(f"The addition of {a} and {b} gives: {add(a,b)}")
    elif user_input==2:
        print(f"Subtracting {a} from {b} gives: {sub(a,b)}")
    elif user_input==3:
        print(f"The multiplication of {a} and {b} gives: {mul(a,b)}")
    elif user_input==4:
        print(f"Dividing {a} from {b} gives: {div(a,b)}" )
    else:
        print("Invalid Input")
    again=input("Perform another? (y/n): ").lower()
    if again!="y":
        break