#Build a Calculator with All Operators:
#Take two numbers as input.
#Print results of: + - * / // % **
#Also show > < == comparisons.
#Print bitwise operations.
x=int(input("Enter the First Number: "))
y=int(input("Enter the Second Number: "))
Opt=input("Enter the operation you want to perform (+,-,*,/,//,%,&,|,^,~,<<,>>): ")
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
elif Opt=="+":
    print(x,"+",y,"is: ",x+y)
elif Opt=="-":
    print(x,"-",y,"is: ",x-y)
elif Opt=="*":
    print(x,"*",y,"is: ",x*y)
elif Opt=="/":
    print(x,"/",y,"is: ",x/y)
elif Opt=="//":
    print(x,"//",y,"is: ",x//y)
elif Opt=="%":
    print(x,"%",y,"is: ",x%y)
else:
    print("Invalid Operator")
if x>y:
    Print(x,"is greater then ",y)
elif x<y:
    print(y,"is greater then ",x)
else:
    print(x,"and ",y,"are equal")