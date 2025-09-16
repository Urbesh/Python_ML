#Write a program using logical operators: Input age, check if person is eligible for college (age between 18–25).
#1 Using "AND" operator
age=int(input("Enter your age to check eligibility: "))
if age>=18 and age<=25:
    print("You are eligiable for collage")
else:
    print("You are not eligiable for collage")

#2 Using "OR" and "NOT" operator

age1=int(input("Enter your age to check eligibility: "))
if not(age<18 or age>25):
    print("You are eligiable for collage")
else:
    print("You are not eligiable for collage")
