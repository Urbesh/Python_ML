#Find union, intersection, and difference of {1,2,3} and {2,3,4}
#Simple Version
a={1,2,3}
b={2,3,4}
diff=a.difference(b)
print(f"The difference between two set is {diff}")
uni=a.union(b)
print(f"The union of two sets is {uni}")
inter=a.intersection(b)
print(f"The intersection of two sets is {inter}")

#User Defined Version
A=input("Enter the set_1 elements: ").split()
S_1=set(A)
B=input("Enter the set_2 elements: ").split()
S_2=set(B)
while True:
    print("The actions you can perform are: \n1. Union\n2. Intersection\n3. Difference\n4. Exit")
    choise=input("Enter the action you want to perform: ").lower()
    if choise=="1" or choise=="union":
        Uni=S_1.union(S_2)
        print(f"The union of two sets is: {Uni}")
    elif choise=="2" or choise=="intersection":
        Inter=S_1.intersection(S_2)
        print(f"The Intersection of two sets is: {Inter}")
    elif choise=="3" or choise=="difference":
        Diff=S_1.difference(S_2)
        print(f"The Difference Between two sets is: {Diff}")
    elif choise=="4" or choise=="exit":
        break
    else:
        print("Invalid Input")