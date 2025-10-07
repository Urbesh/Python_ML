#Write a function that accepts variable-length arguments (*args) and prints their sum
def Sum(*args):
    total=sum(args)
    print("Sum of the numbers present in the list is: ",total)
user_input=input("Enter as many number as you want separated by a space: ")
input_list=user_input.split()
num_list=list(map(int,input_list))
Sum(*num_list)