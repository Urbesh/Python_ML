#Print Fibonacci series up to N terms.
#Using While loop
n1=int(input("Enter the Nth term: "))
print("The Fibonacci series is:", end=" ")
a, b = 0, 1
count=0
while count<n1:
    print(a,",",end=" ")
    a,b=b,a+b
    count+=1
print()#Start a new line after the series
print("This output is generated using While Loop")
#Using For loop
N=int(input("Enter the Nth term: "))
print("The Fibonacci Series is: ", end=" ")
A,B=0,1
for count in range(N):
    print(A,",",end=" ")
    A,B=B,A+B
print()#Start a new line after the series
print("This output is generated using For Loop")