# dct_example = {'key1':'value1', 'key2':'value2', 'key3':'value3' }

# print(dct_example['key1'])

# print(dct_example.get('key2'))
# dct_example['key4'] = 'surpriseValue'
# for x in dct_example:
#     print(f'key: {x} value: {dct_example[x]}')

# dct_example['key4'] = 'value4' 
# print('key6' in dct_example)

# del dct_example['key4']
# print(dct_example)
# dct_example.popitem()
# print(dct_example)

# # change the dictionary into a list of tuples
# tuples_example = dct_example.items()
# print(tuples_example)

# # clearing a dictionary 
# # print(dct_example.clear())

# dct_copy  = dct_example.copy()
# for x in dct_copy:
#     print(f'key: {x} value: {dct_copy[x]}')

# keys = dct_example.keys()
# print(keys)

# value = dct_example.values()


dog = {}

dog['name'] = 'tray'
dog['colour'] = 'black'
dog['breed'] = 'pibble'
dog['legs'] = '3'
dog['age'] = '12'

print(dog)

student_dct = {"firstname":'Tamjid' , 
               "lastname":"Islam", 
               "gender":"male", 
                "age": "17",
                "marital_status":"single",
                "skills":["organised", "analytical"],
                "country":'united kingdom',
                'city':'london',
                'address':"fhf2223"
                }

student_dct['skills'].append('resourceful')
for x in student_dct:
    print(f"{x} : {student_dct[x]}")

STkeys = list(student_dct.keys())
print(f"the keys: {STkeys}")
STvalues = list(student_dct.values())
print(f'the values: {STvalues}')
print("Tuple form")
print(student_dct.items())

del(student_dct['address'])
print(student_dct)
del dog


