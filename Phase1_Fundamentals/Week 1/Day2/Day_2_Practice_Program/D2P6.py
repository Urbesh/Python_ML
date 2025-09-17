#Play with bitwise operators: Show results of X & Y, X | Y, X ^ Y, ~X, X << Y, X >> Y.
x=int(input("Enter the First Number: "))
y=int(input("Enter the Second Number: "))
Opt=input("Enter the bitwise operation you want to perform (&,|,^,~,<<,>>): ")
if Opt=="&":
    print(x,"&",y,"=",x&y)
elif Opt=="|":
    print(x,"|",y,"=",x|y)
elif Opt=="^":
    print(x,"^",y,"=",x^y)
elif Opt=="~":
    print("~",x,"=",~x)
elif Opt=="<<":
    print(x,"<<",y,"=",x<<y)
elif Opt==">>":
    print(x,"<<",y,"=",x>>y)
else:
    print("Invalid Operator")