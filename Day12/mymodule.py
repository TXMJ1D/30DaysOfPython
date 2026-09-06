# functions to use in exercises in main file 
import random
import string
import random

def random_user_id(chars,ids):
    for _ in range(ids):
        characters = string.ascii_letters + string.digits
        user_id = "".join(random.choice(characters) for _ in range(chars))
        print(user_id)

def get_user_input():
    chars = int(input("Enter the number of characters in your id: "))
    ids = int(input("Enter the number of ids you wish to generate: "))
    return chars, ids

colour_range = []
def rgb_colour_gen():
    for x in range(0,256):
        colour_range.append(x)
    rgb_vals = [random.choice(colour_range) for _ in range(3)]
    return rgb_vals

# exercise 2 

hexvals = string.hexdigits
def list_of_hexacolours(num):
    for x in range(num):
        hex_result = "".join(random.choice(hexvals) for _ in range(6))
        print(hex_result)
    
def get_hexnum():
    user_input = int(input("Enter the number of hexadecimals values you want: "))
    return user_input

def list_of_rgbcolours(num):
    for x in range(0,256):
        colour_range.append(x)
    for y in range(num):
        rgb_list = [random.choice(colour_range) for _ in range(3)]
        print(rgb_list)
def get_rgb_num():
    user_input = int(input("Enter the number of rgb values you want: "))
    return user_input

def generate_colours(type):
    if type == "rgb":
        result = list_of_rgbcolours(get_rgb_num())
    elif type == "hex":
        result= list_of_hexacolours(get_hexnum())
    else:
        return 'invalid input'
    return result 

def get_type():
    user_input = input('Enter the type of colours you wish to generate: [rgb/hex] ')
    return user_input

def shuffle_list(list):
    # count = 0
    # for x in range(count,len(list)):
    #     for y in range(x+1,len(list)-1):
    #         list[x], list[y] = list[y], list[x]
    #         count+=1
    #         if count == len(list):
    #             return list

    for x in range(len(list)):
        y = random.randint(0,len(list)-1)
        list[x], list[y] = list[y], list[x]
    return list

def randint_generator():
    int_list = []
    for x in range(7):
        z = random.randint(0,9)
        if z not in int_list:
            int_list.append(z)
    return int_list