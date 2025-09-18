#Absolute Value : Input a number, print its absolute value (without using abs()).
num=float(input("Enter a number: "))
if num<0:
    abs_value=-num
else:
    abs_value=num
print(f"The absolute value of {num} is {abs_value}.")