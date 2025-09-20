#Count how many times an element appears in a list.
#Simple Version
A=["Apple", "Banana", "Orange", "Banana", "Pineapple", "Banana", "Orange"]
To_count="Banana"
count=A.count(To_count)
print(f"The element {To_count} appeared in the list for {count} time")

#User Defined Version
a=input("Enter the list elements (string) followed by a space: ").split()
print("The list: ",a)
to_count=input("Enter the element who's number of occurrence you want to find: ")
Count=[x.lower() for x in a].count(to_count.lower())
print(f"The element {to_count} appeared in the list for {Count} time")