# converting into tuples
# Syntax: tuple(sequence)

#Example 1: converting string into tuple.
color = "Red"
tuple_a = tuple(color)
print(tuple_a)      #Output:('R', 'e', 'd')

#Example 2: range into tuple
tuple_a = tuple(range(4))
print(tuple_a)      #Output:(0, 1, 2, 3)

#Example 3: list into tuple
list_a = [1, 2, 3]
tuple_a = tuple(list_a)
print(tuple_a)      #Output:(1, 2, 3)