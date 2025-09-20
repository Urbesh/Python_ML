#Reverse a list (without using reverse())
a=[]
n_elements=int(input("Enter the number of elements you want to have in your list: "))
for i in range(n_elements):
    elements=input(f"Enter the element {i+1}: ")
    a.append(elements)
print("List  is: ",a)
length=len(a)
rev=length-1
rev_list=[]
while rev>=0:
    rev_element=a[rev]
    rev_list.append(rev_element)
    rev-=1
print("The reversed list is: ",rev_list)