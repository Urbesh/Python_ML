#Electricity Bill Calculator
#Units entered by user:
#First 100 units → ₹5/unit
#Next 100 units → ₹7/unit
#Above 200 → ₹10/unit
units=int(input("Enter the number of units consumed: "))
if units<=100:
    bill=units*5
elif units<=200:
    bill=(100*5)+(units-100)*7
else:
    bill=(100*5)+(100*7)+(units-200)*10
print(f"Total electricity bill: ₹{bill}")