#Divisible by X and Y: Check if number is divisible by both or if the number is just by any one number.
num = int(input("Enter a number: "))
x = int(input("Enter the first divisor (X): "))
y = int(input("Enter the second divisor (Y): "))
if num % x==0 and num % y==0:
    print(f"The number {num} is divisible by both {x} and {y}.")
elif num % x==0 and num % y!=0:
    print(f"The number {num} is divisible by {x} but not by {y}.")
elif num % x!=0 and num % y==0:
    print(f"The number {num} is divisible by {y} but not by {x}.")
else:
    print(f"The number {num} is not divisible by both {x} and {y}.")