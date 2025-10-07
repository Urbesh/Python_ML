#Write a function that uses a lambda to double each element in a list.
def my_double(n):
    return lambda a:a*n
my_function=my_double(2)
user_input=input("Enter as many numbers as you want separated by a space: ")
input_list=user_input.split()
num_list=list(map(int,input_list))
print(f"The entered list of numbers are: {num_list}")
double_num=[]
for i in num_list:
    double=my_function(i)
    double_num.append(double)
print(f"The list after doubling each number of the list: {double_num}")