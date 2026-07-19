#exercise 1 

print("Day 2: 30 Days of Python Programming")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"
country = input("Enter your country: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
year = input("Enter the current year: ")
is_married = input("Are you married? ")
if is_married == "yes":
    is_true = True
else:
    is_true = False

bool(is_true)
is_light_on = input("Are your lights on? ")
if is_light_on == "yes".lower():
        print("Woohoo your lights are on!!")
else:
    print("It is dark")

print("Here are your credentials: ")
print(f"first name: {first_name}")
print(f"last name: {last_name}")
print(f"full name: {full_name}")
print(f"country: {country}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Year: {year}")
print(f"Married: {is_true}")

#exercise 2 
print("Data Types:")
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(country))
print(type(city))
print(type(year))
print(type(is_true))

print(len(first_name))

len_fn = len(first_name)
len_ln = len(last_name)
if len_fn < len_ln:
     print("last name name is longer than first name!!!")
else:
    print("first name is longer than last name")

num_one = 5 
num_two = 4

print(type(num_one))

total  = num_one + num_two
diff = num_two-num_one
product = num_one * num_two
division = num_one/num_two

remainder = num_two%num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("calculations:")
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

print("Circle Problem")
radius = 30
area_of_circle = 3.14 * (radius**2)
circumference = 3.14 * (radius*2)
print(f"area of given circle: {area_of_circle}")
print(f"circumference of given circle: {circumference}")
user_radius = int(input("Enter a radius: "))
user_cirlce_area = 3.14 * (user_radius**2)
print(f"User circle area: {user_cirlce_area}")
