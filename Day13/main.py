# # List comprehension
# # Syntax: [expression for i in iterable if condition]

# # example 1: one way of converting a string to a list 
# language = "Python"
# lst = list(language)
# print(type(lst))
# print(lst)

# # second way (list comprehension)
# lst = [i for i in language]
# print(type(lst))
# print(lst)

# # example 2: generate lists of numbers
# numbers = [i for i in range(11)]
# # list of squared of numbers up to 12
# numbers2 = [i * i for i in range(12)] 
# # list of tuples: number and theyre square counterpart
# numbers3 = [(i, i*i) for i in range(11)]

# example 3: list comprehension can be combined with if statements 
# even_numbers = [i for i in range(22) if i % 2 == 0]
# odd_numbers = [i for i in range(22) if i % 2 != 0]

# numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
# # print all positive even numbers from this list using set comprehension
# pos_even_nums = [i for i in numbers if i>0 and i%2 == 0]
# print(pos_even_nums)

# flatten lists:
# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatten_list = [number for row in list_of_lists for number in row]

# lambda functions:

# def add_two_nums(x,y):
#     return x + y

# lamda
# add_two_nums = lambda a, b: a+b
# print(add_two_nums(2,3))

# self invoking lambda function
# print((lambda a,b: a+b)(2,3))

# square = lambda x: x**2
# print(square(3))

# cube =  lambda x: x**3
# print(cube(5))

# lambda within a function

# def power(x):
#     return lambda n: x ** n

# print(power(2)(6))


# exercise 1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero = [i for i in numbers if i <= 0]
print(neg_zero)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

lst_of_powers = [(i,i**0,i**1,i**3,i**4,i**5,i**6) for i in range(11)]
print(lst_of_powers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst_countries = [[country,city] for row in countries for country,city in row]
print(lst_countries)
flattened_ctrs = [country for row in lst_countries for country in row]
print(flattened_ctrs)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst_names = [[fn,sn] for row in names for fn, sn in row]
print(lst_names)
flattened_names = [name for row in lst_names for name in row]
print(flattened_names)

gradient = lambda x1,y1,x2,y2: (y2-y1) / (x2-x1)
def user_coords():
    x1 = int(input("Enter the 1st x coordinate: "))
    y1 = int(input("Enter the 1st y coordinate: "))
    x2 = int(input("Enter the 2nd x coordinate: "))
    y2 = int(input("Enter the 2nd y coordinate: "))
    return x1,y1,x2,y2

print(gradient(*user_coords()))

# countries2 = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# dct_ctrs = [{'country': country, 'city': city} for row in countries2 for country,city in row]
# print(dct_ctrs)
# retry in the morning (5)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_dict = [{'country': country, 'city': city} for row in countries for country,city in row]
print(countries_dict)