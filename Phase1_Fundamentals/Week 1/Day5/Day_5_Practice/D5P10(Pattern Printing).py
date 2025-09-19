#Print this number triangle:
# 1
# 12
# 123
# 1234
#Using For loop
n=4
for i in range (1,n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
print("This output is generated using for loop")
#Using While loop
n=4
i=1
while i<=n:
    j=1
    while j<=i:
        print(j, end="")
        j+=1
    print()
    i+=1
print("This output is generated using while loop")