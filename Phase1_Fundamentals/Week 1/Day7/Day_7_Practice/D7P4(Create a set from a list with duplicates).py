#Create a set from a list with duplicates
#Simple version
A=["Apple", "Banana", "Apple", "Orange", "Apple", "Pineapple", "Banana", "Orange", "Cherry"]
S=set(A)
print(S)

#User Defined version
a=input("Enter the list elements (enter duplicate elements): ").split()
s=set(a)
print(f"Converting a list to set will remove all the duplicate elements: {s}")