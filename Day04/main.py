name = "tamjid"
first_letter = name[0]
print(first_letter)
second_letter = name[1]
print(second_letter)
last_index = len(name) - 1
last_letter = last_index
#another way to find the last letter is to use negative indexing
#eg.
last_letter2 = name[-1]
second_last_letter = name[-2]

#String Methods 
# capitalize() - converts the first character into a capital first_letter
# count() - returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
# endswith() - checks if a string ends with a specified ending
# expandtabs() - replaces tab character with spaces, default tab size is 8, it takes a number as an argument for tab size
# find() - returns index of the first occurence a substring, if not found: returns -1
# rfind() - returns index of the last occurence of a substring, if not found returns -1
# format() - formats string into a nicer output 
# index() - returns the lowest index of a substring, additional arguments indicate starting and ending index 
# isalnum() - checks alphanumeric character 
# isalpha() - checks if all string elements are alphabet characters (a-b)
# isdecimal - checks if all characters in a string are decimal (0-9)
# isdigit() - checks if all characters in a string are numbers (0-9 and some other unicode characters)
# isnumeric() - checks if all characters in  a string are numbers or number related (like isdigit() just accepts more symbols)
# isidentifier() - checks for a valid identifier - checks if a string is a valid variable name 
# islower() - checks if all alphabet characters are lowercase
# isupper() - same as islower() checks for uppercase 
# join() - returns a concatenated string 
# strip() - removes all given string at the start and end of a String
# replace() - replaces a substring with a given String
# split() - split the string, using given string or space as a seperator
# title() - returns a title case string (capitalised words like a title)
# swapcase() - converts all uppercase characters to lower case and vice versa 
# startswith() - checks if string starts with the specified string

#exercise

string_one = "thirty"
string_two = "days"
string_three = "of"
string_four = "python"
sentence = [string_one, string_two, string_three, string_four]
result = ' '.join(sentence)
result = result.capitalize()
print(result)

string_5  = "coding"
replace_string = "python"
string_6 = "for"
string_7 = "all"
company = replace_string + " " + string_6 + " " + string_7
# company = company.upper()
# company = company.capitalize()
# company = company.title()
# company = company.swapcase()
print(company)
print(f'Length of the company name: \n     {len(company)} characters')

print(len(string_5))
company_cut  =  company[7:14]
print(company_cut)

is_coding  = company.find("coding")
print(is_coding)

split_company = company.split(" ")
print(split_company)

tech_orgs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
split_techOrgs = tech_orgs.split(",")
print(split_techOrgs)
print(company[0])
print(company[-1])
print(company[10])

letter_pos = company.index("p")
print(letter_pos)
print(company.rfind("l"))

example_sentence = "you cannot end a sentence with because because because is a conjunction"
print(example_sentence.index("because"))
print(example_sentence.find("because"))
print(example_sentence.rfind("because"))


start = example_sentence.find("because")
end = example_sentence.rfind("because") + len("because")

new_sentence = example_sentence[:start] + "because" + example_sentence[end:]
print(f'your new sentence is: \n {new_sentence}')

print(example_sentence.find("because"))

coding_sentence = "coding for all"
coding_sentence = coding_sentence.title()
print(coding_sentence)

if coding_sentence.find("Coding") == 0:
    print("It does start with the substring: Coding")
else:
    print("no the sentence does not start with the substring: Coding")

if coding_sentence.find("coding") == 0:
    print(" test 2: It does start with the substring: Coding")
else:
    print("test 2: no the sentence does not start with the substring: Coding")

test_string = '   Coding For All      ' 
test_string = test_string.strip()
print(test_string)


list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " ".join(list1)
print(list1)

list2 = ['God of war', 'Need for speed', 'Apex Legends' , 'Fortnite', 'Call of Duty']
result2 = " ".join(list2)
print(result2)


print("I \n am enjoying this challenge")
print("I \n just wonder what is \n next.")

row1 = "Name\t Age\t Country\t City"
row1 = row1.expandtabs(8)
print(row1)
row2 = "Asabenah\t 250\t Finland\t Helsinki"
row2 = row2.expandtabs(2)
print(row2)

radius = 10
area = 3.14*radius**2
print(f'The area of a circle with radius {radius} is {area} meters squared')

sum = 8 + 6 
subt = 8 - 6
mult = 8 * 6 
div = 8 / 6 
quot = 8 % 6 
rem = 8 // 6 
ind = 8 ** 6 
print(f"8 + 6 = {sum} \n8 - 6 = {subt} \n8 * 6 = {mult} \n8 / 6 = {div} \n8 % 6 = {quot} \n8 // 6 = {rem} \n8 ** 6 = {ind}")
