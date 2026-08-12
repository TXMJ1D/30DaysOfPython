# Tuples
# Exercise 1 
empty_tuple = ()

games_tuple = ("call of duty", 'fortnite', 'apex legends', 'ghost of tsushima')
print(len(games_tuple))
print(games_tuple)
console_tuple  = ('Playstation', 'Xbox', 'Nintendo Switch', 'PC')
combo_tuple = console_tuple + games_tuple
print(combo_tuple)
print(len(combo_tuple))
genre_tuple = ('horror', 'shooter', 'fps', 'story' )
final_tuple = genre_tuple + combo_tuple
print(final_tuple)

# Exercise 2 

print(final_tuple[:4])

fruits = ('apple', 'orange', 'kiwi', 'pineapple', 'pomegranate', 'watermelon')
vegetables = ('brocolli','carrot','lettuce','sprouts')
animal = ('lamb','cow','lobster')
food_stuff_tuple = fruits+vegetables+animal
print(food_stuff_tuple)
food_stuff_tuple = list(food_stuff_tuple)
print(food_stuff_tuple)
del food_stuff_tuple[len(food_stuff_tuple) // 2]
del food_stuff_tuple[:3]

del food_stuff_tuple
tuple_final = ('one','two','three','four')
print("five" in tuple_final)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
