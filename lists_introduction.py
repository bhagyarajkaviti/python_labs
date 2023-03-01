#LIST: Holds an ordered sequence of items
# list is createed by enclosing elements with in [square] brackets.Each item is seperated by a comma "," .
a = 2  
list_a = [5, "six", a, 8.2]
print(type(list_a))
print(list_a)
print(len(list_a)) # length of the list

list_b = [1, list_a]
print(list_b) 

print(list_a[1]) #Accessing list elements, we use indexing

#Iterating over a list:
for item in list_a:
    print(item)