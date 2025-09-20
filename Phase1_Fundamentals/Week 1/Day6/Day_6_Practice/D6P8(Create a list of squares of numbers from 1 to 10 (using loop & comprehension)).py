#Create a list of squares of numbers from 1 to 10 (using loop & comprehension)
from math import pow
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(f"The squre of {i} is: {pow(i,2)}")