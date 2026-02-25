# Program to find area and perimeter of a triangle
import math
# Input sides of the triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Perimeter calculation
perimeter = a + b + c

# Semi-perimeter
s = perimeter / 2

# Area calculation using Heron's formula
# Area = √(s(s-a)(s-b)(s-c))

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Perimeter of the triangle:", perimeter)
print("Area of the triangle:", area)
print("Sides of the triangle: a =", a, ", b =", b, ", c =", c)