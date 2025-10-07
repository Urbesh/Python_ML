#Write a function square() that takes a list and returns a new list with squares using map()
import math
def square(n):
    return lambda a:pow(a,n)
user_input=input("Enter the as many number as you want separated by a space: ")
user_Str_input=user_input.split()
#since we can't directly take integer type value, we will convert it to integers.
num_list=list(map(int,user_Str_input))
my_square=square(2)
Square_num=[]
for i in num_list:
    elements=my_square(i)
    Square_num.append(elements)
print(f"The new list after performing square operation: {Square_num}")