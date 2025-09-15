#Write a script to take user input and print type of each variable.
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height in centimeters: "))
print("Hello, my name is", name + ", I am", age, "years old and my height is", height, "cm.")
print("Data types are:", type(name), type(age), type(height))