#Print this pattern: 
# *
# **
# ***
# ****
#Using For loop
n=4
for i in range(n):
    print("*"*(i+1))
print("This Output is generated using For loop")
#Using While loop
N=4
I=1
while I<=n:
    print("*"*I)
    I+=1
print("This Output is generated using While loop")