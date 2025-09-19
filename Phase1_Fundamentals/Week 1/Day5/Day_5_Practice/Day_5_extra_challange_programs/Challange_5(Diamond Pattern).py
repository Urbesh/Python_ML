#Diamond Pattern
n=7
i=1
while i<=n:
    space=(n-i)//2
    print(' '*space+'*'*i)
    i+=2
i=n-2
while i>0:
    space=(n-i)//2
    print(' '*space+'*'*i)
    i-=2