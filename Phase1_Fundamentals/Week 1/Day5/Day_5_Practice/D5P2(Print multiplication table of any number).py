#Print multiplication table of any number
#Using While loop
n1=int(input("Enter any number: "))
n2=1
while n2<=10:
    print(n1,"*", n2, "=",n1*n2)
    n2=n2+1
print("This output is generated using while loop")
#Using For loop
n1=int(input("Enter any number: "))
for n2 in range(1,11):
    print(n1,"*",n2,"=",n1*n2)
print("This output is generated using for loop")
