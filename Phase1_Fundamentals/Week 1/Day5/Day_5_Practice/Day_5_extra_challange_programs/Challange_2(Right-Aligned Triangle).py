#Right-Aligned Triangle
n=4
for i in range(n):
    print(' '*(n-i-1)+'*'*(i+1))
print("Using for loop")
#Using while loop
N=4
I=1
K=N-1
while I<=N:
    print(' '*(K)+'*'*(I))
    K=N-I-1
    I+=1
print("Using while loop")