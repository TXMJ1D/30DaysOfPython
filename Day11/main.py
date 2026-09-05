# Functions day 11

# def add_two_numbers(num1,num2):
#     sum = num1 + num2
#     return sum

# def main():
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a second number: "))
#     print("Your result is: ")
#     print(add_two_numbers(num1,num2))

# main()

# def area_of_circle(radius):
#     area = radius*radius*3.14
#     return area

# def main():
#     radius = int(input("Enter the radius of your circle: "))
#     print("Here is the area of your circle")
#     print(area_of_circle(radius))

# main()

# arbitary parameters
# num = []
# def add_all_numbers(*num):
#     sum = 0 
#     for i in num:
#         sum += i
#     return sum

# def getnum():
#     while True:
#         user_num = int(input('Enter a number: ')) 
#         num.append(user_num)
#         choice = input("Would you like to exit the program: ")
#         if choice == "yes":
#             print("Thats all your numbers!!")
#             break
#         else:
#             print("Adding more numbers")
#             continue

# def main():
#     getnum()
#     result = add_all_numbers(*num)
#     print(result)

# main()

# def degrees_to_faren(value):
#     faren = (value * 9 / 5) + 32
#     return faren

# def main():
#     value = int(input("Enter the temperature in degrees: "))
#     result = degrees_to_faren(value)
#     print(f'Your temperature in farenheit is: {result}')

# main()

# summer = ['march', 'april', 'may' 'june', 'july']
# spring = ['august, september']
# autumn = ['october', 'november']
# winter = ['december','january','february']

# def check_season(input):
#     if input in summer:
#         return 'summer'
#     if input in spring:
#         return 'spring'
#     if input in autumn:
#         return 'autumn'
#     if input in winter:
#         return 'winter'
#     else:
#         print("Invalid month!!")

# def get_season():
#     user_input = input("Enter a month: ")
#     return user_input

# def main():
#     month = get_season()
#     result = check_season(month)
#     print(f"You are in: {result}")


# main()

# def calculate_slope(x1,y1,x2,y2):
#     gradient = (y2-y1)/(x2-x1)
#     return gradient

# def get_coords():
#     x1 = int(input("Enter point 1 x coordinate: "))
#     y1 = int(input("Enter point 1 y coordinate: "))
#     x2 = int(input("Enter point 2 x coordinate: "))
#     y2 = int(input("Enter point 2 y coordinate: "))
#     print(f"Your coordinates are: ({x1},{y1}) and ({x2},{y2})")
#     return x1,y1,x2,y2

# def main():
#     result = calculate_slope(*get_coords())
#     print("Your gradient is: ")
#     print(result)

# main()
# import math

# def calc_quad_solutions():
#     a=int(input("Enter the value of a: "))
#     b = int(input("Enter the value of b: "))
#     c = int(input("Enter the value of c: "))
#     discriminant = (b**2) - (4*a*c)
#     if discriminant > 0:
#         x1 = (-b + math.sqrt(discriminant))/(2*a)
#         x2 = (-b - math.sqrt(discriminant)) / (2*a)
#         return x1, x2
#     else:
#         return "No valid solutions as the discriminant is a negative value:"

# def main():
#     result = calc_quad_solutions()
#     print(f"Your solutitions are: {result} ")

# main()

# vals = []
# def print_list(*vals):
#     for x in vals:
#         print(x)

# def get_vals():
#     while True:
#         user_input = input("Enter an item for the list: ")
#         vals.append(user_input)
#         choice = input('Would you like to exit the program: [yes/no] ')
#         if choice == "yes":
#             print("You have chosen to exit the program: ")
#             return vals
#         else:
#             print("You continue:")
#             continue

# def main():
#     result = print_list(*get_vals())
#     print("Here is your result:")
#     print(result)

# main()
# vals = []
# reverse_vals = []
# def reverse_list(*vals):
#     for x in range(len(vals)-1,-1,-1):
#         reverse_vals.append(vals[x])
#     return reverse_vals


# def get_vals():
#     while True:
#         user_input = input("Enter an item for the list of values: ")
#         vals.append(user_input)
#         choice = input("Would you like to exit the program: [yes/no] ")
#         if choice == 'yes':
#             return vals
#         else:
#             continue

# def main():
#     result = reverse_list(*get_vals())
#     print("Here are your results: ")
#     print(result)

# main()

# foods = ['tomato','cucumber','spaghetti','noodles']
# animals = ['tiger', 'lion', 'koala']

# def add_list(value,list):
#     if value not in list:
#         list.append(value)
#     else:
#          print(f'{value} already exists in that list')
# def remove_item(value, list):
#     if value in list:
#         val_index = list.index(value)
#         list.pop(val_index)
#     else:
#         print(f"That item does not exist in {list}")

# def main():
    # user_input = input("Enter the item you wish to add to the list: ")
    # which_list = input("WHhich list: [animals/foods] ")
    # if which_list == 'foods':
    #     add_list(user_input,foods)
    #     print(foods)
    # elif which_list == 'animals':
    #     add_list(user_input,animals)
    #     print(animals)
    # else:
    #     print("Invalid list!!")
#     print(f"Animals: = {animals}")
#     print(f'foods: {foods}')
#     print()
#     user_input = input("Enter the item you wish to remove from the list: ")
#     which_list = input("WHhich list: [animals/foods] ")
#     if which_list == 'foods':
#         remove_item(user_input,foods)
#         print(foods)
#     elif which_list == 'animals':
#         remove_item(user_input,animals)
#         print(animals)
#     else:
#         print("Invalid list!!")

# main()


# str_list = []
# cap_list = []

# def capitalise_list_items(*vals):
#     for x in str_list:
#         cap_list.append(x.capitalize())
#     return cap_list


# def get_list():
#     while True:
#         user_input = input("Enter a string to add to the list: (uncapitalised) ")
#         str_list.append(user_input)
#         choice = input("Would you like to exit the program: [yes/no] ")
#         if choice == 'yes':
#             print("You have exited the program!!")
#             return str_list
#         else:
#             continue

# def main():
#     result = capitalise_list_items(*get_list())
#     print("Here are your results")
#     print(result)

# main()


# def sum_of_numbers(x):
#     sum = 0
#     for i in range(0,x+1):
#         sum += i
#     return sum

# def sum_of_odds(x):
#     sum = 0
#     for i in range(0,x+1):
#         if i % 2 != 0:
#             sum += i
#     return sum

# def sum_of_evens(x):
#     sum = 0
#     for i in range(0,x+1):
#         if i % 2 == 0:
#             sum += i
#     return sum

# def get_int():
#     user_input = int(input("Enter an integer for the sum in the range of your input: "))
#     return user_input

# def main():
#     # result = sum_of_numbers(get_int())
#     # result = sum_of_odds(get_int())
#     result = sum_of_evens(get_int())
#     print(f"Here is your result: \n {result}")

# main()

# Exercise level 2 

# def evens_and_odds(x):
#     count_evens = 0
#     count_odds = 0
#     for i in range(0,x+1):
#         if i % 2 == 0:
#             count_evens += 1
#         elif i % 2 != 0:
#             count_odds += 1
#     return f"number of evens: {count_evens} \n number of odds: {count_odds}"

# def get_int():
#     user_input = int(input("Enter an integer: "))
#     return user_input 

# def main():
#     result = evens_and_odds(get_int())
#     print(result)

# main()

# def calc_factorial(x):
#     total = 1
#     for i in range(1,x+1):
#         total *= i 
#     return total

# def get_int():
#     user_input = int(input("Enter an integer: "))
#     return user_input

# def main():
#     result = calc_factorial(get_int())
#     print("Here is your factorial: ")
#     print(result)

# main()

# list1 = []
# list2 = [1,2,3,4,5,5,5,6,6,7,7,8,8,9,23,454,67]
# print("Here are your lists:")
# print("list1")
# print(list1)
# print("list2")
# print(list2)

# def is_empty(list):
#     if len(list) == 0:
#         return f"{list} is empty"
#     else:
#         return f'{list} is not empty'

# def get_list():
#     user_input = input("Enter the name of your list you wish to check: ")
#     if user_input == "list1":
#         return list1
#     elif user_input == "list2":
#         return list2
#     else:
#         return "invalid list"

# def main():
#     result = is_empty(get_list())
#     print(result)

# main()

# from statistics import mode
# from statistics import variance
# import math


# list2 = [1,2,3,4,5,5,5,6,6,7,7,8,8,9,23,454,67]

# def calculate_mean(list):
#     sum = 0
#     for i in list2:
#         sum += i
#     mean = sum / len(list)
#     return mean

# def calculate_mode(list):
#     mode_result = mode(list)
#     return mode_result

# def calculate_median(list):
#     median_place = len(list)//2
#     median = list[median_place]
#     return median

# def calculate_range(list):
#     range = list[-1] - list[0]
#     return range 

# def calculate_variance(list):
#     var = variance(list)
#     return var 

# def calculate_stand_dev(list):
#     var2 = variance(list)
#     st_deviation = math.sqrt(var2)
#     return st_deviation

# def main():
#     print("Here is your list: ")
#     print(list2)
#     while True:
#         choice1 = input("What would you like to calculate: \n mean, mode, median, range, variance or std(standard deviation) ")
#         if choice1 == "mean":
#             result = calculate_mean(list2)
#             print(result)
#         elif choice1 == "mode":
#             result = calculate_mode(list2)
#             print(result)
#         elif choice1 == "median":
#             result = calculate_median(list2)
#             print(result)
#         elif choice1 == 'variance':
#             result = calculate_variance(list2)
#             print(result)
#         elif choice1 == 'std':
#             result = calculate_stand_dev(list2)
#             print(result)
#         else:
#             print("invalid choice..")
#         choice2 = input("Would you like to exit the program? ")
#         if choice2 == 'yes':
#             print("You have exited the program.. ")
#             break
#         else:
#             print("You continue")
#             continue

# main()

# def greet():
#     user_input = input("Would you like to input a name? [yes/no]  ")
#     if user_input == 'yes':
#         user_input2 = input("Enter your name: ")
#         return f'Hello {user_input2}'
#     elif user_input == 'no':
#         return 'Hello guest!'
#     else:
#         return 'invalid input'

# def main():
#     result = greet()
#     print(result)
# main()

# def show_args(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')

# def main():
#     show_args(name='tamjid', hair='black', age=19)

# main()

# Exercise Level 3:

# def is_prime(num):
#     if num < 2:
#         return False
#     elif num >= 2:
#         for i in range(2,num):
#             if num %  i == 0:
#                 return False
#         return True

# def get_num():
#     user_input = int(input("Enter a number: "))
#     return user_input

# def main():
#     result = is_prime(get_num())
#     print("Result: Is Prime?")
#     print(result)

# main()

# uq_list = []
# rand_list = ["bike",'apple','banana','strawberry', 'bike']

# def is_unique(list):
#     for x in list:
#         cnt = list.count(x)
#         if cnt == 1:
#             uq_list.append(x)
#     return uq_list

# def main():
#     result = is_unique(rand_list)
#     print("The following values are unique in the given list")
#     print(result)

# main()

same_list = []
rand_list = ["bike",'apple','banana','strawberry', 'bike']
rand_list2 = ["bike", 2.1, 'apple','banana', True, 'strawberry', 2, 'bike']
print(rand_list)
print(rand_list2)

# def is_same_type(list):
#     for x in list:
#         for j in list:
#             if type(x) != type(j):
#                 same_list.append(x)
#     if len(same_list) != 0:
#         return 'NOT Same Type'
#     else:
#         return 'Same Type'

# Reworked answer:
# def is_same_type(list):
#     for x in list:
#         if type(x) != type(list[0]):
#             return 'Not Same Type'
#     return "same type"

# def main():
#     result = is_same_type(rand_list)
#     result2 = is_same_type(rand_list2)
#     print("Result 1")
#     print(result)
#     print('Result 2')
#     print(result2)

# main()

# def valid_variable(user_input):
#     if user_input.isidentifier():
#         return True
#     else:
#         return False

# def get_variable():
#     user_input = input("Enter your chosen variable name: ")
#     return user_input

# def main():
#     result = valid_variable(get_variable())
#     if result:
#         print("Valid variable name")
#     else:
#         print("Invalid variable name!!")
    
# main()
