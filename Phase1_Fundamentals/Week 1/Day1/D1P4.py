#BMI Calculator
height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kilograms: "))
bmi=weight/height**2
print("Your BMI is: ",bmi)
if bmi<16:
    print("You are Severely Underweight")
elif 16<=bmi<17:
    print("You are Moderately Underweight")
elif 17<=bmi<18.5:
    print("You are Mildly Underweight")
elif 18.5<=bmi<25:
    print("You are Normal")
elif 25<=bmi<30:
    print("You are Overweight")
elif 30<=bmi<35:
    print("You are Obese Class I")
elif 35<=bmi<40:
    print("You are Obese Class II")
else:
    print("You are Obese Class III")
