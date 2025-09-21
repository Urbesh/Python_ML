#Create a tuple of 5 elements, print first and last.
#Simple version
a=("Apple", "Banana", "Orange", "Pineapple", "Cherry")
print(f"The First element of the tuple is: {a[0]}")
print(f"The Last element of the tuple is: {a[4]}")

#User defined version
A=()
L=list(A)
n_elements=int(input("Enter the number of Elements you want in your Tuple: "))
for i in range(n_elements):
    elements=input(f"Enter the element {i+1}: ")
    L.append(elements)
    A=tuple(L)
print(f"The elements present in the tuple are: {A}")
print(f"The first element of the Tuple is: {A[0]}")
t_len=len(A)
last=t_len-1
print(f"The last element of the Tuple is: {a[last]}")