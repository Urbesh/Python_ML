#Print all prime numbers between X and Y.
#Using While Loop
x=int(input("Enter the Starting term: "))
y=int(input("Enter the Nth term: "))
print("All prime numbers between", x, "and", y, "are:", end=" ")
i=x
while i<=y:
    if i>1:
        is_prime=True
        j=2
        while j<=int(i ** 0.5):
            if i % j == 0:
                is_prime=False
                break
            j+=1
        if is_prime:
            print(i, end=", ")
    i += 1
print() #Start a new line
print("This output is generated using While loop")
#Using For loop
X=int(input("Enter the Starting term: "))
Y=int(input("Enter the Nth term: "))
print("All prime numbers between", x, "and", y, "are:", end=" ")
for I in range(X,Y+1):
    if I>1:
        prime=True
        for J in range(2,int(I**0.5)+1):
            if I%J==0:
                prime=False
                break
        if prime:
            print(I,end=", ")
print() #Start a new line
print("This output is generated using While loop")