#Use filter() to extract even numbers from a list.
user_input=input("Enter as many number as you want separated by space: ")
input_list=user_input.split()
num_list=list(map(int,input_list))
def even(n):
    if n%2==0:
        return True
    else:
        return False
Storage=[]
#Why this Storage list? 
# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not
# In simple words if I directly print the values stored in Even variable the in would get something like this "<filter object at 0x00000255C8D5B9A0>"
Even=filter(even,num_list)
for i in Even:
    Storage.append(i)
print(f"The entered list of numbers are: {num_list}")
print(f"Even numbers present in the list are: {Storage}")