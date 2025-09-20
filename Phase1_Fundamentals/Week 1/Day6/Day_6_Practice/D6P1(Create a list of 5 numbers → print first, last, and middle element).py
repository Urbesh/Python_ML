#Create a list of 5 numbers → print first, last, and middle element.
#Simple Version
A=["Apple", "Banana", "Orange", "Pineapple", "Cherry"]
print("The First Elelment of the List is: ",A[0])
print("The Middle Element of the list is: ",A[2])
print("The Last Element of the list is ",A[4])

#User input version
a=[]
n_elements=int(input("Enter the number of elements you want to have in your list: "))
for i in range(n_elements):
    elements=input(f"Enter the element {i+1}: ")
    a.append(elements)
print("List: ",a)
print("The First Element of the list is: ",a[0])
middle_index_1=(len(a)//2)-1
middle_index_2=(len(a)//2)
middle_element_even=[a[middle_index_1],a[middle_index_2]]
last_index=(len(a)-1)
if n_elements%2==0:
    print("The MIddle Element of the list is: ",middle_element_even)
else:
    print("The Middle Element of the list is: ",a[middle_index_2])
print("The Last Element of the list is: ",a[last_index])
