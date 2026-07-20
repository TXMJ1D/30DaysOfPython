#Exercise Day 3 - Operators 
import random 
import math

age = int(19)
print(type(age))

height = float((input("Enter yout height in Feet (floating point): ")))
real_part  = random.uniform(-10,10)
imaginary_part = random.uniform(-10,10)
complex_num = complex(real_part,imaginary_part)
print(f"Complex Number: {complex_num}")

#Area of a triangle 
base = int(input("Enter a base for triangle: "))
height = int(input("Enter a height for triangle: "))
area_of_triangle = float(0.5 * base * height)
print(f"Area of Triangle: {area_of_triangle}")

#Perimeter of triangle 
side_a  = int(input("Enter side A: "))
side_b = int(input("Enter side B: "))
side_c  = int(input("Enter side C: "))
perimeter_triangle = side_a + side_b + side_c
print(f"Perimeter of Triangle: {perimeter_triangle}")

#Rectangle 
rectangle_side_base = int(input("Enter side A of Rectangle: "))
rectangle_side_height = int(input("Enter side B of Rectangle: "))
area_rectangle = rectangle_side_base*rectangle_side_height
rectangle_perimeter = 2*(rectangle_side_height+rectangle_side_base)

print(f'area of rectangle: {area_rectangle}')
print(f'perimeter of a rectangle: {rectangle_perimeter}')

#Circle
circle_radius = int(input("Enter a radius of cirlce: "))
area_circle = 3.14 * circle_radius**2 
circumferemce_circle  = circle_radius*2 * 3.14
print(f'Area of circle: {area_circle}')
print(f'circumference of circle: {circumferemce_circle}')

#Gradient of a line
gradient_one  = 2 
x1 = 2
x2 = 6
y1 = 2
y2 = 10
gradient_two = (y2-y1)/(x2-x1)
print(f"Gradient 2: {gradient_two}")

euclidean_dist = math.sqrt(((x1-y1)**2)+((x2-y2)**2))
print(f'Pythagorean distance: {euclidean_dist}')

print("Comparing gradients:")
if gradient_one < gradient_two:
    print("Line 2 is steeper due to a higher gradient")
elif gradient_one > gradient_two:
    print("Line 1 is steeper due to a higher gradient")
else:
    print("Gradients are equal")

#Comparing string:
string_one = "dragon"
string_two = "python"
print(f"Length of {string_one} is  {len(string_one)}")
print(f"Length of {string_two} is  {len(string_two)}")

if "on" in string_two and string_one:
    print("True")
else:
    print("False")

string_three = "I hope this course is not full of jargon"
if "jargon" in string_three:
    print("True")
else:
    print("False")

len_string_two = len(string_two)
float(len_string_two)
str(len_string_two)

#Arithmetic
result = 7//3 
print(result)
if result == 2.7:
    print(f"They are equal")
else:
    print('they are not equal')

string_int = type("10")
int_ = type(10)
if int_ == string_int:
    print("they are the same")
else:
    print("they are not the same")

#Salary/wage problem
hours = int(input("Enter your hours for the working day: "))
hr_pay = int(input("Enter your hourly pay: "))
wage_day = hours * hr_pay
weekly_earning = wage_day*7
print(f'Your wage is: {wage_day}')
print(f"Your weekly earning is: {weekly_earning}")

#number of seconds in year problem
years_lived = int(input("Enter the number of years you have lived: "))
seconds_lived = years_lived * 60 * 60 * 24 * 365 
print(f"You have lived {seconds_lived} seconds!")

#table problem

for i in range(1,6):
    print(i, i**0, i*1, i*3, i*4, i*5)