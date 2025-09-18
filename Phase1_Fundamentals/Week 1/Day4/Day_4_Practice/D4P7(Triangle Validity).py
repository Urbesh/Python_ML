#Triangle Validity
#Input 3 sides → check if they can form a triangle.
#Bonus: Check if it’s equilateral, isosceles, or scalene.
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        triangle_type = "equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
    print(f"The sides form a valid triangle which is {triangle_type}.")
else:
    print("The sides do not form a valid triangle.")