print("Day 2: 30 Days of Python Programming")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"
country = input("Enter your country: ")
city = input("Enter your city: ")
age = input("Enter your age: ")
year = input("Enter the current year: ")
is_married = input("Are you married?")
if is_married == "yes":
    is_true = True
else:
    is_true = False

is_light_on = input("Are your lights on?")
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