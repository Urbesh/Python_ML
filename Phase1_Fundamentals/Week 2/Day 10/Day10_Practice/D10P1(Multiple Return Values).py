'''
Multiple Return Values:
Write a function that takes two numbers and returns their sum, difference, and product.
'''
def cal(a,b):
    Sum=a+b
    Diff=a-b
    Pro=a*b
    return Sum,Diff,Pro
a=int(input("Enter First number: "))
b=int(input("Enter Second Input: "))
sum_val,diff_val,pro_val=cal(a,b)
print(f"Sum: {sum_val}, Difference: {diff_val}, Product: {pro_val}")