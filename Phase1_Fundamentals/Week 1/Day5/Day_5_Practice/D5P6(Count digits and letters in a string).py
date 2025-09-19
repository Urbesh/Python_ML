#Count digits and letters in a string.
#Using While loop
s=input("Enter a String: ")
count_digit=0
count_alpha=0
i=0
while i<len(s):
    if s[i].isdigit():
        count_digit+=1
    elif s[i].isalpha():
        count_alpha+=1
    i+=1
print("The number of digits present in the String is: ",count_digit)
print("The number of alphabets present in the String is: ",count_alpha)
print("This output is generated using While loop")

#Using For loop
S=input("Enter a String: ")
count_dig=0
count_alp=0
for char in S:
    if char.isdigit():
        count_dig+=1
    elif char.isalpha():
        count_alp+=1
print("The number of digits present in the String is: ",count_dig)
print("The number of alphabets present in the String is: ",count_alp)
print("This output is generated using For loop")