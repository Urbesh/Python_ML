'''''
🧱 Mini Project: “Safe Calculator v2”

🔧 Goal: Build a robust calculator that uses functions + exception handling to prevent crashes.

🎯 Features:

Takes two numeric inputs

Supports +, -, *, /

Handles:

Division by zero

Invalid operator

Non-numeric input

Uses functions for each operation

Keeps running until user chooses to exit
'''''

def sum_if_plus_present(s):
    if '+'in s:
        parts=s.split('+')
        total_sum=0
        for part in parts:
            try:
                total_sum+=float(part.strip()) #Converts to float and add 
            except ValueError:
                # Handle cases where a part is not a valid number
                return 0  # Or raise an error, or handle differently
        return total_sum
    else:
        return 0
def sub_if_sub_is_present(n):
    if '-'in n:
        parts2=n.split('-')
        sub=0
        for part2 in parts2:
            try:
                sub-=float(part2.strip()) #Converts to float and sub 
            except ValueError:
                return 0
        return sub
    else:
        return 0
def mul_if_star_is_present(m):
    if '*' in m:
        parts3=m.split('*')
        mul=1
        for part3 in parts3:
            try:
                mul*=float(part3.strip()) #Converts to float and multiply
            except ValueError:
                return 0
        return mul
    else:
        return 0
def div_if_slash_is_present(d):
    if '/' in d:
        parts4 = d.split('/')
        try:
            div = float(parts4[0].strip())
            for part4 in parts4[1:]:
                div /= float(part4.strip()) ##Converts to float and divide
            return div
        except ValueError:
            return 0
        except ZeroDivisionError:
            return "Error: Division by zero!"
    else:
        return 0
while True:
    user_input=input("Enter the equation (Don't even try to enter equations like (4+78(65*5)/2)): ")
    if '+' in user_input:
        result1=sum_if_plus_present(user_input)
        print(f"The sum of the number(s): {result1}")
    elif '-' in user_input:
        result2=sub_if_sub_is_present(user_input)
        print(f"The difference of the number(s): {result2}")
    elif '*' in user_input:
        result3=mul_if_star_is_present(user_input)
        print(f"Multiplying the number(S) results: {result3}")
    elif '/' in user_input:
        result4=div_if_slash_is_present(user_input)
        print(f"The result is: {result4}")
    else:
        print("Invalid Operation!")
    again=input("Perform another? (y/n): ").lower()
    if again!="y":
        break