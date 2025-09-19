#Sum of first N natural numbers.
#Using While loop
n1=int(input("Enter the Nth number: "))
n2=1
sum=0
while n2<=n1:
    sum+=n2
    n2=n2+1
print("The Sum of N natural numbers is: ",sum)
print("This Output is generated using While loop")

#Using For loop
N1=int(input("Enter the Nth number: "))
Sum=0
for N2 in range(1,N1+1):
    Sum+=N2
    N2=N2+1
print("The Sum of N natural numbers is: ",Sum)
print("This Output is generated using for loop")