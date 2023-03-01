animals = ['cat', 'dog']
wild_animals = ['Tiger', 'Fox']
animals += [wild_animals]
print(animals)
print(len(animals)) # gives length as 3. as the animals list contains 3 items. Here [wild_animals] list is considered as single item in concatinated animal list.

animals = ['cat', 'dog']
animals += wild_animals
print(animals)
print(len(animals)) # gives length as 4.as the animals list contains 4 items