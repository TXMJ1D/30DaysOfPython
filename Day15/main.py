# Type errors

# Example 1: SyntaxError
#   forgetting to enclose a string in parenthesis
# print("hello"
# SyntaxError: '(' was never closed

# print("Hello")

# Example 2: NameError
#    name "variable" is not defined 

# print(age)
# NameError: name 'age' is not defined
# age = 15
# print(age)

# Debugged the error by defining the variable name 
#   which in this case was age 

# Example 3: IndexError
#   Invalid list indexes used: Out of range values 
# list = [1,2,3,4]
# # print(list[4])
# # IndexError: list index out of range
# print(list[3])

# Example 4: ModuleNotFoundError 
#   incorrect spelling or invalid methods imported:
    # eg. randoms instead of random or maths instead of math 

# import maths

# print(math.sqrt(16))
# ModuleNotFoundError: No module named 'maths'

# import math 

# print(math.sqrt(16))
# Fixed the importing of math and now we can use the math functions

# Example 5: AttributeError
#   using incorrect or mispelling attributes from modules 
#   therefore python raises an error and tells us it does not exist within the module 

# import math
# print(math.squareroot(16))
# AttributeError: module 'math' has no attribute 'squareroot'
# print(math.pi)
# Spelt and used the correct attribute that exists inside of the math module allowing the code to run with no errors


# Example 6: KeyError
#   error in the key when returning a value from a dictionary - typo or invalid key 

# dict_random = {"Name": "Tamjid", "Age": 13, "Country": "United Kingdom"}
# # print(dict_random['name'])
# # KeyError: 'name'
# print(dict_random["Name"])
# # code is debugged by fixing the typo


# Example 7: TypeError
#   Occurs when trying to perform logical operations between 2 different data types such as
#   between a string and an integer

# rand_int = "12"
# sum = rand_int + 4
# print(sum)
# TypeError: can only concatenate str (not "int") to str

rand_int = "12"
sum = int(rand_int) + 4
print(sum)

# debugged by converting the rand_int variable into an integer to allow for the addition of 2 integers

# Example 8: ImportError
#   importing the wrong functions (as a oppose to using the wrong one like the earlier error type) from a module

# from math import power

# power_int = 2.power(3)
# ImportError: cannot import name 'power' from 'math' 

# from math import pow
# power_int = pow(3,2)
# print(power_int)

# Debugged by importing the correctly named function from the module math

# Example 9: ValueError
#   When trying to convert a data type however it is not possible as the value does not allign with the type
    # eg. "12S" to an integer is not possible due to the string "s"

# variable_rand = "12S"
# print(int(variable_rand))
# ValueError: invalid literal for int() with base 10: '12S'

# variable_rand = 12
# print(type(str(variable_rand)))

# Example 10: ZeroDivisionError
#   Error that arises when trying to divide an integer by zero which produces an impossible to compute imaginary number
# div_rand  = 12/0
# print(div_rand)
# ZeroDivisionError: division by zero

div_rand = 0/12
print(div_rand)