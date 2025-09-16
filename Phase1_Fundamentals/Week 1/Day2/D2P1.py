#Take two numbers as input, show results of: Addition, Subtraction, Multiplication, Division, Floor division, Modulus, Power.
n1=float(input("Enter First Number: "))
n2=float(input("Enter Second Number: "))
ch=input("Choose the operation you want to perform (Addition, Subtraction, Multiplication, Division, Floor division, Modulus, Power.): ")
if ch=="Addition" or ch=="Add" or ch=="addition" or ch=="add":
    print("The addition of ",n1," and ",n2," is: ",n1+n2)
elif ch=="Subtraction" or ch=="Sub" or ch=="subtraction" or ch=="sub":
    print("The subtraction of ",n1," by ",n2," is: ",n1-n2)
elif ch=="Multiplication" or ch=="Mul" or ch=="multiplication" or ch=="mul":
    print("The multiplication of ",n1," and ",n2," is: ",n1*n2)
elif ch=="Division" or ch=="Div" or ch=="division" or ch=="div":
    print("The division of ",n1," by ",n2," is: ",n1/n2)
elif ch=="Floor" or ch=="Flo" or ch=="floor" or ch=="flo":
    print("The floor division of ",n1," by ",n2," is: ",n1//n2)
elif ch=="Modulus" or ch=="Mod" or ch=="modulus" or ch=="mod":
    print("The modulus division of ",n1," by ",n2," is: ",n1%n2)
else:
    print(n1,"to the power",n2," is: ",n1**n2)
