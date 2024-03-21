#Area of Triangle.

#he area of a triangle can be calculated using different formulas depending on the information you have about
# the triangle. One common method is using Heron's formula, which requires knowing the lengths of all three
# sides of the triangle. Another method is using the base and height of the triangle. Below, I'll provide
# a Python program to calculate the area of a triangle using the base and height:

def triangle_area(base, height):
    return 0.5 * base * height

# Test the function
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = triangle_area(base, height)
print("The area of the triangle with base", base, "and height", height, "is", area)
