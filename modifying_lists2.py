#Example 1:
countries_1 = ["India", "Australia", "America"]
countries_2 = countries_1
countries_1 = countries_1 + ["Italy", "France"]

print("Countries 1 : "+ str(countries_1))   #Output: Countries 1 : ['India', 'Australia', 'America', 'Italy', 'France']
print("Countries 2 : "+ str(countries_2))   #Output: Countries 2 : ['India', 'Australia', 'America']

#Example 2:
list_a = ["H", ["A", "R"], "R"]
list_b = list_a[1]
list_b = list_b + ["y"]
print(list_a)   #Output: ['H', ['A', 'R'], 'R']
print(list_b)   #Output: ['A', 'R', 'y']

#Example 3:
characters = [1, 2, 3, ["!", "@", "#"]]
print(characters[3][2]) #Output: #

#Example 4:
even_numbers = [0, 2, 4, 6, 8]
id_1 = id(even_numbers)
even_numbers[0] = 10
id_2 = id(even_numbers)
is_same_id = (id_1 == id_2)
print(is_same_id)   #Output: True