#Swap Two Variables Without using a third variable.
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
print("Before swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("After swapping a=",a,"b=",b)
