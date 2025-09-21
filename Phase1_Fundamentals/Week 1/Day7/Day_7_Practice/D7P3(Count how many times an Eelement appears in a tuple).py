#Count how many times an element appears in a tuple
#Simple Version
A=("Apple", "Banana", "Apple", "Orange", "Pineapple", "Apple", "Cherry", "Apple")
To_count="Apple"
Count=A.count(To_count)
print(f"{To_count} appeared in the tuple for {Count} time")

#User Defined Version
a=input("Enter the Tuple Elements followed by a space: ").split()
t=tuple(a)
print(f"The tuple is: {t}")
to_count=input("Enter the Element who's number of appearance you want to check: ")
count=t.count(to_count)
print(f"{to_count} appeared in the tuple for {count} time")