#Factorial of a number.
#Using While loop
n1=int(input("Enter any number to calculate its Factorial: "))
n2=1
mul=1
while n2<=n1:
    mul*=n2
    n2=n2+1
print("The Factorial of",n1,"is:",mul)
print("This output is generated using While loop")
#Using For loop
N1=int(input("Enter any number to calculate its factorial: " ))
Mul=1
for N2 in range(1,N1+1):
    Mul*=N2
    N2=N2+1
print("The Factorial of",N1,"is:",Mul)
print("This output is generated using For loop")