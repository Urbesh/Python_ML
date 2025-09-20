#Add an element at the end and at a specific index
#Simple Version
A=["Apple", "Banana", "Orange", "Cherry", "Pineapple"]
A.insert(1,"Cake")
print(A)

#User Defined Version
a=[]
n_elements=int(input("Enter the number of elements you want in your list: "))
for i in range(n_elements):
    elements=input(f"Enter the Element {i+1}: ")
    a.append(elements)
print("List is: ",a)
while True:
    choise = input("Do you want to add more element to the list (Y/N): ")
    if choise.lower()=="y":
        usr_index=int(input("Enter the index number where you want to enter the element: "))
        usr_element=input("Enter the Element you want to insert: ")
        a.insert(usr_index, usr_element)
        print("The updated list is:", a)
    elif choise.lower()=="n":
        break
    else:
        print("Invalid Input")
        break