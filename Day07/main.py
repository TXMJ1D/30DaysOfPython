it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# print(len(it_companies))
# it_companies.add("Twitter")
# print(it_companies)
it_companies.update(["Tesla", "Claude", "OpenAi"])
print(it_companies)
it_companies.remove("Tesla")
pop_item = it_companies.pop()
print(pop_item)
print(it_companies)

# what is the difference between remove and discard?


# Exercise 2 

C = A.union(B)
print(C)

inters = A.intersection(B)
print(inters)

print(A.issubset(B))
print(A.isdisjoint(B))
set1 = A.update(B)
set2 = B.update(A)
print(f'{set1} \n{set2}')

print(A.symmetric_difference(B))
del set1
del set2 

set_age = set(age)
print(f'List: {len(age)} \nSet: {len(set_age)}')
# set removes repeated elements
print(age)

# a string is a collection of characters, a tuple is an immutable ordered collection of elements, a list is a mutable collection of elements

rand_str = "I am a teacher and I love to inspire and teach people"
rand_str_list = rand_str.split(" ")
rand_str_set = set(rand_str_list)
print(rand_str_set)