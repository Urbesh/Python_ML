#alculate Area of Circle
#using math module
import math
rad=float(input("Enter radius of circle: "))
area=math.pi*rad**2
print("Area of circle is: ",area)

#using user defined function
pi=22/7
def area_of_circle(r):
    area=pi*r**2
    return area
radius=float(input("Enter radius of circle: "))
print("Area of circle is: ",area_of_circle(radius))
