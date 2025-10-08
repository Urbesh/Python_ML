'''
Return Type Conversion:
Function that takes a string and returns the number of digits in it.
'''
String=input("Enter any strings including numbers separated by space: ").split()
def num_counter(s):
    count=0
    for i in String:
        if i.isnumeric():
            count+=1
    return count
num_string=num_counter(String)
print(f"The number of digits present in the string is: {num_string}")