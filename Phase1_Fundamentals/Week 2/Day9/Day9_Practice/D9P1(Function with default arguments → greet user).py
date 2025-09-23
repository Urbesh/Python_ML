#Function with default arguments → greet user
def greet(name="User"):
    print(f"Hello {name}, WELCOME to Python")
usr_input=input("Enter your name (Press Enter if you don't want to share your name): ")
if usr_input.strip() == "":
    greet()   
else:
    greet(usr_input)
