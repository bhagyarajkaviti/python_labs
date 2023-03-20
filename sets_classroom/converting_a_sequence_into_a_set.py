#Syntax : `set(sequence)`
#Takes any sequence as argument and converts to set, avoiding duplicates.

#Example 1: list
set_a = set([1, 2, 3, 1, 2, 4, 6, 2, 1])
print(set_a)            #Output:{1, 2, 3, 4, 6}
print(type(set_a))      #Output:<class 'set'>

#Example 2:string
set_a = set("apple")
print(set_a)            #Output:{'p', 'a', 'l', 'e'}
print(type(set_a))      #Output:<class 'set'>

set_a = set((1, 2, 3, 1, 2, 4, 6, 2, 1))
print(set_a)            #Output:{1, 2, 3, 4, 6}
print(type(set_a))      #Output:<class 'set'>


