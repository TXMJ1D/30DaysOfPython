# High order functions 

# handling functions as parameters
# returning functions as return values from another function
# using python closures as decorators

# 1: function as a parameter
def sum_num(nums):
    return sum(nums)

def higher_order_function(f,lst): #takes a function as a parameter
    summation = f(lst)
    return summation

result = higher_order_function(sum_num,[1,2,3,4,5])
print(result)

# 2: function as a return value 

def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x >= 0:
        return x 
    else:
        return -(x)
    
def higher_order_functions2(f,num):
    if f == "square":
        return square(num)
    elif f == "cube":
        return cube(num)
    elif f == "absolute":
        return absolute(num)

result2 = higher_order_functions2("cube",2)
print(result2)

# error here, strayed off track and did not realise i did not produce a function as a value 
# correction

def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x >= 0:
        return x 
    else:
        return -(x)
    
def higher_order_functions2(f):
    if f == "square":
        return square
    elif f == "cube":
        return cube
    elif f == "absolute":
        return absolute

result2 = higher_order_functions2("cube")
print(result2(2))

# 3: Python closures

# what is a closure
    # python allows a nested function to access
    # the outer scope of the enclosing function
    # this is known as a Closure

    # in python, closure is created by nesting a function inside of another
    # encapsulating function 
    # and then returning the inner function

# def add_ten():
#     ten = 10
#     def add(num):
#         return num + ten
#     return add

def add_nine():
    nine = 9 
    def add(num):
        return nine + num
    return add

closure_result = add_nine()
print(closure_result(9))

# Python DECORATORS
# a decorator is a design pattern in python that allows a user to add new functionality 
# to an existing object without modifying its structure

    # creating decorators - we need an outer function with an inner wrapper function

# def greeting():
#     return 'Welcome to Python'

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_upper = func.upper()
#         return make_upper
#     return wrapper

# # testing 
# # g = uppercase_decorator(greeting)
# # print(g())
# # implementing the decorator 
# @uppercase_decorator
# def greeting():
#     return 'Welcome to python'

# print(greeting())

    # Applying multiple decorators to a function

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase 
#     return wrapper 

# def split_the_string(function):
#     def wrapper():
#         func = function()
#         splt_string = func.split()
#         return splt_string
#     return wrapper

# @split_the_string
# @uppercase_decorator

# def greeting():
#     return 'hello my name is tamjid'
# print(greeting())

    # Accepting Parameters in Decorator Functions 

def decorator_with_parameter(function):
    def wrapper_with_parameter(para1,para2,para3):
        function(para1,para2,para3)
        print("I live in {}".format(para3))
    return wrapper_with_parameter

@decorator_with_parameter
def print_full_name(firstname,lastname,country):
    print("I am {} {}, I love to do boxing in my free time".format(firstname,lastname))

print_full_name("Tamjid","Islam","United Kingdom")

# Built in High Order Functions
# 1: Python - Map Function
#   takes a function and iterable as a parameter

# numbers = [1,2,3,4,5]

# def square(x):
#     return x ** 2

# numbers_squared = map(square,numbers)
# print(list(numbers_squared))

# # Now try it using lambda 

# numbers2 = [1,2,3,4,5,6]
# numbers_squared = map(lambda x : x**2, numbers2)
# print(list(numbers_squared))

# # Map function - example 2 

# names = ["Tamjid", "James", "Holsten", "Yuzuki"]

# def change_to_upper(name):
#     return name.upper()

# names_upper = map(change_to_upper,names)
# print(list(names_upper))

# Now with lambda

names = ["Tamjid", "James", "Holsten", "Yuzuki"]
names_upper = map(lambda name : name.upper(), names)
print(list(names_upper))

# The built in high order function, Map, iterates over a list and returns a new list


# The Filter Function
# the filter() function calls the specified function created by the user, which returns a boolean for each item of the specified iterable (list) 
    # it filters the items that satisfy the filter criteria 


nums = [1,2,4,5,6,5,67]

def is_even(num):
        if num % 2 == 0:
            return True 
        else:
            return False 

even_nums = filter(is_even,nums)
print(list(even_nums))

def is_odd(num):
    if num%2 != 0:
        return True 
    else:
        return False 

odd_nums = filter(is_odd,nums)
print(list(odd_nums))

# Reduce Function - built-in high order function 
    # reduce() function is defined in functools module
        # like map and filter, it takes 2 parameters (a function and an iterable)
        # it does not return another iterable and instead returns a single value
    
# 1. 
# numbers_str = ['1','2','4','3','5']

# def add_int(x,y):
#     return int(x) + int(y)

# total = reduce(numbers_str,add_int)
# print(total)

# reduce function does not work maybe it is not built in vscode??

# Exercise 1 


# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names2 = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 1. map function takes 2 parameters, a function and an iterable (list) it iterates over the list
#     # and returns a new list, filter function takes a function which returns a boolean for each item and an iterable
#         # it iterates over the list using the specified function and returns values that meeet the criteria of the function
#     # and the reduce function also takes 2 parameters including a function and an iterable and returns a single value

# # 2. High order functions are functions that take other functions as parameters,
# #   a decorator is a design pattern in python that allows a user to add new functionality to an object without 
#     # modifying its structure, a closure is nesting a function inside another encapsulating function and returning the inner function (as in the use of decorators and wrapping inside of decorator functions)

# # 3. call function for map, filter or reduce
# countries = ['China', 'Slovakia', 'Estonia', "Paraguay", "Vatican City", "England"]
# def upper_countries(country):
#     return country.upper()

# uppercaseCountries = map(upper_countries,countries)
# print(list(uppercaseCountries))

# # 4
# for country in countries:
#     print(country)

# for x,country in enumerate(countries):
#     print(f"{x+1}: {country}")
# print()
# # 5.
# for x,name in enumerate(names2):
#     print(f'{x}: {name}')
# print()
# # 6.
# for x,number in enumerate(numbers):
#     print(f'{x}: {number}')


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names2 = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercise 2

# 1.
def change_to_uppercase(country):
    return country.upper()

upper_country = map(change_to_uppercase,countries)
print(list(upper_country))

# 2
def square_num(z):
    return z**2
square_numbers = map(square_num,numbers)
print(list(square_numbers))

# 3
def names_upper(name):
    return name.upper()

uppercase_names = map(names_upper,names2)
print(list(uppercase_names))

# 4
def filterout_land(country):
    if "land" not in country:
        return True
    else:
        return False 

country_noland = filter(filterout_land,countries)
print(list(country_noland))

# 5 
def no_long_country(country):
    if len(country) == 6:
        return False
    else:
        return True 

short_string_countries = filter(no_long_country,countries)
print(list(short_string_countries))

# 6
# string = "hello"
# print(string[0])
def no_e_starter(country):
    if country[0] == 'E':
        return False
    else:
        return True 

filtered_Country = filter(no_e_starter,countries)
print(list(filtered_Country))

from functools import reduce 

numbers_str = ['2','2','4','5','5']
def add_ints(x,y):
    return int(x)+int(y)

output_sum = reduce(add_ints,numbers_str)
print(output_sum)

# 7.
# chain 2 or more 
even_squares = filter(lambda x : x%2 == 0, 
                      map(lambda x : x ** 2, numbers))
print(list(even_squares))

reduced_total_of_squared_evens = reduce(lambda x,y: x + y,
                                        filter(lambda x : x%2 == 0,
                                               map(lambda x : x**2, numbers)))
print(reduced_total_of_squared_evens)
 
# 8.
def get_string_list(item):
    return str(item)

str_items_list = map(get_string_list, numbers)
print(list(str_items_list))

# 9.

def add_numbers(x,y):
    return x + y 

total_numbers = reduce(add_numbers,numbers)
print(total_numbers)

# 10.
def concatenate_countries(x,y):
    return f"{x}, {y}" 

concatenated_list = reduce(concatenate_countries,countries)
print(f'{concatenated_list} are all north European countries')

# 11.
countries2 = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

def countries_end_in_land(country):
    if "land" in country:
        return True 
    else:
        return False 

filtered_list = filter(countries_end_in_land,countries2)
print(list(filtered_list))

def countries_start_P(country):
    if country[0] == "P":
        return True 
    else:
        return False 

filtered_list2 = filter(countries_start_P,countries2)
print(list(filtered_list2))

# 12. 

def count_countries(countries):
    dict_countries = {}
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in dict_countries:
            dict_countries[first_letter] += 1
        else:
            dict_countries[first_letter] = 1 
    return dict_countries

print(count_countries(countries2))

# 13.
def get_first_ten(countries):
    ten_countries = []
    for x in range(0,10):
        ten_countries.append(countries[x])
    return ten_countries

print(get_first_ten(countries2))

def get_last_ten(countries):
    last_ten_countries = []
    for x in range(-10,0,1):
        last_ten_countries.append(countries[x])
    return last_ten_countries

print(get_last_ten(countries2))