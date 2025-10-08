'''''
ValueError Catching:
Handle invalid inputs (like letters when expecting numbers)
'''''
def get_num_input(n):
    while True:
        user_input=input(n)
        try:
            num=int(user_input)
            return num
        except ValueError:
            print("Invalid Input!")
age=get_num_input("Please Enter your age: ")
hight=get_num_input("Please enter your hight: ")
print(f"Your age is {age} and your hight is {hight}")