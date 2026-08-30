# conditionals 

# while True:
#     age = int(input('enter your age: '))
#     if age > 18:
#         print('You are old enough to drive!!')
#     else:
#         remYrs = 18 - age 
#         print(f"you have {remYrs} years left until you can drive") 
    
#     choice = input('Do you wish to exit the program? ')
#     if choice == "yes":
#         print('You have now exited the program!!!')
#         break
#     else:
#         print("You chose to continue!!")
#         continue


# my_age = 19
# print("Hi i am your personal age assistant, i am" + " " + str(my_age), "years old!!")


# while True:
#     your_age = int(input("Enter your age: "))
#     if your_age < 1:
#         print("That is not a valid age")
#     elif your_age > 1 and your_age < my_age:
#         print(f"Wow you are {your_age} years old and {my_age-your_age} years younger than me")
#     elif your_age > 1 and your_age > my_age:
#         print(f"Wow you are {your_age} years old and {your_age-my_age} older than me!!")
#     elif your_age == 1:
#         print(f"Wow you a year old and {my_age-your_age} years younger than me")
#     elif my_age == your_age:
#         print("We are the same age!!")
#     else:
#         print("That is an invalid age")
    
#     choice = input("Would you like to exit the program [yes/no] ")
#     if choice.lower() == 'yes':
#         print('you have now exited the program')
#         break
#     else:
#         print("You chose to stay!!!")
#         continue

# while True:
#    a = int(input('Enter your first number: ')) 
#    b = int(input('Enter a second number: '))
#    if a < b:
#         print(f"a: {a} is larger than b: {b}")
#    elif a > b:
#        print(f"b: {b} is larger than a: {a}")
#    elif a == b:
#        print(f"a: {a} is equal to b: {b}")

#    choice = input("Would you like to exit the program? [yes/no] ")
#    if choice.lower() ==  "yes":
#        print("You have exited the program")
#        break
#    else:
#        print("You chose to continue: ")
#        continue
   

# exercise 2

# A = []

# B = []

# C = []

# D = []

# F = []


# for x in range(90,101):
#     A.append(x)
# for x in range(80,90):
#     B.append(x)
# for x in range(70,80):
#     C.append(x)
# for x in range(60,70):
#     D.append(x)
# for x in range(0,60):
#     F.append(x)

# while True:
#     user_input = int(input('Enter your score out of 100: '))
#     print("Calculating your grade: ")
#     if user_input in A:
#         print("Your grade is an A")
#     if user_input in B:
#         print("Your grade is a B")
#     if user_input in C:
#         print("Your grade is a C")
#     if user_input in D:
#         print("Your grade is a D")
#     if user_input in F:
#         print("Your grade is F")
#     else:
#         print("Invalid score!")
    
#     choice = input("Would you like to exit the program? [yes/no] ")
#     if choice.lower() == "yes":
#         print("You have exited the program")
#         break
#     else:
#         print("You have continued")
#         continue
    
# autumn = ["September","October","November"]
# winter = ["December","January","February"]
# spring = ["March","April","May"]
# summer = ["June","July","August"]

# while True:
#     print("Season Provider: ")
#     user_input = input("Please Enter a Month: ")
#     if user_input.capitalize() in autumn:
#         print(f"You are in the month {user_input}: \nThe season is Autumn")
#     if user_input.capitalize() in winter:
#         print(f'You are in the month {user_input}:\nThe season is Winter')
#     if user_input.capitalize() in spring:
#         print(f'You are in the month of {user_input}:\nThe season is Spring')
#     if user_input.capitalize() in summer:
#         print(f'You are in the month {user_input}:\nThe season is Summer')
#     else:
#         print("Invalid month!!!")

#     choice = input("Would you like to exit the program: [yes/no] ")
#     if choice.lower() == "yes":
#         print("You have now exited the program:")
#         break
#     else:
#         print("You chose to continue: ")
#         continue


#  Exercise 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


if 'skills' in person:
    print("Yes the key: Person exists")
    mid = len(person['skills'])//2
    print(person['skills'][mid])

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python exists in the skills key")
        print('Python' in person['skills'])

if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and "React" in person["skills"]:
    print("This person is a frontend developer")

if len(person['skills']) == 3 and "Python" in person['skills'] and 'MongoDB' in person['skills'] and 'Node' in person['skills']:
    print("This person is a backend developer")

if len(person['skills']) == 3 and 'MongoDB' in person['skills'] and 'Node' in person['skills'] and 'React' in person['skills']:
    print("This person is a full-stack developer")
else:
    print("Unknown Title")

if person['is_married'] == True and person['country'] == 'Finland':
    print("Asebeneh Yetayeh lives in Finland. He is Married!")