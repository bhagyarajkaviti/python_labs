#COncatination of lists: Similar to strings '+' operator concatinates lists
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]

list_c = list_a + list_b
print(list_c)
print(len(list_c))

list_c = list_a + [list_b] # here list_b items is considered as single item in list_c.
print(list_c)
print(len(list_c))