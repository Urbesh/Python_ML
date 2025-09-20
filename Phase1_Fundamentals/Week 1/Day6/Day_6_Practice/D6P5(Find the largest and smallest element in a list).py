#Find the largest and smallest element in a list.
a=input("Enter the list elements (String) followed by a space: ").split()
print("List is: ",a)
largest_element=max(a, key=len)
smallest_element=min(a, key=len)
print(f"The Largest Element of the list is: {largest_element}")
print(f"The Smallest Element of the list is: {smallest_element}")