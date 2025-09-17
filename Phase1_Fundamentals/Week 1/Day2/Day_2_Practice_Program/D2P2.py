#Check if a number is greater than another, and if they are equal.
n1=float(input("Enter First Number: "))
n2=float(input("Enter Sercond Number: "))
if n1>n2:
    print(n1,"is Greater than",n2)
elif n1<n2:
    print(n2,"is Greater than",n1)
else:
    print(n1,"and",n2,"are equal")