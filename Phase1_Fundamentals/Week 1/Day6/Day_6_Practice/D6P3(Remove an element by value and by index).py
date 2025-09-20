#Remove an element by value and by index
#Simple Version
A=["Apple", "Banana", "Orange", "Banana", "Pineapple", "Cherry"]
A.remove("Banana")
print(A)
A.pop(2)
print(A)

#User Defined Version
a=[]
n_elements=int(input("Enter the number of elements you want to have in your list: "))
for i in range(n_elements):
    elements=input(f"Enter the Element {i+1}: ")
    a.append(elements)
print("List is: ",a)
choise=input("Do you want to remove element from the list (Y/N): ")
while True:
    if choise.lower()=="y":
        usr_choise=input("Enter the index number or the element you want to remove: ")
        if usr_choise.isdigit():
            index=int(usr_choise)
            if 0<=index<len(a):
                a.pop(index)
                print("Updated List: ",a)
            else:
                print("Invalid Index")
        else:
            if usr_choise in a:
                a.remove(usr_choise)
                print("Updated List: ",a)
            else:
                print("Element not found")
    choise = input("Do you want to remove element from the list (Y/N): ")
    if choise.lower()!="y":
        break