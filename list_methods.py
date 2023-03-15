#Adding items to list
#Example 1: append() ===> Adds an element to the end of the list.
# syntax: list.append(value)
list_a = []
for x in range(1,4):
    list_a.append(x)    
print(list_a)  #Output:[1, 2, 3]  
 
#Example 2: extend() ===> Adds all the elements of a sequence to the end of the list.
# Syntax: list_a.extend(list_b)
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print(list_a)   #Output:[1, 2, 3, 4, 5, 6]  

#Example 3: insert() ===> element is inserted to the list at specified index.
# Syntax: list.insert(index,value)
list_a = [1, 2, 3]
list_a.insert(1, 4)
print(list_a)   #Output:[1, 4, 2, 3]


#Removing items from the list

#Example 4: pop() ===> removes the last element in a list.
#Syntax: list.pop()
list_a = [1,2,3,4,5,6]
list_a.pop()
print(list_a)   #Output:[1, 2, 3, 4, 5]

#Example 5: remove() ===> removes the first matching element from the list.
# Syntax: list.remove(value)
list_a = [1, 3, 2, 3, 4]
list_a.remove(3)
print(list_a) #Output:[1, 2, 3, 4]

#Example 6: clear() ===> Removes all the items from the list
# Syntax: list.clear()
list_a = [1, 2, 3, 4, 5, 7]
list_a.clear()
print(list_a)   #Output:[]

#Miscellaneous

#Example 7: index() ===> Returns the index at the first occurence of the specified value.
# Syntax: list.index(value)
list_a = [1, 3, 2, 3]
find_index = list_a.index(3)
print(find_index) #output:1

#Example 8: count() ===> Returns the number of elements with the specified value.
# Syntax : list.count(value)
list_a = [1, 2, 3, 4, 5, 2, 2, 7, 9, 2, 7, 2]
counts = list_a.count(2) #value 2 has occured 5 times in the list. 
print(counts)   #output:5

#Example 9: sort() vs sorted()
#syntax: list.sort()
list_a = [1, 3, 2, 5, 4]
sorted(list_a)
print(list_a)       #Output:[1, 3, 2, 5, 4]
list_b = sorted(list_a)
print(list_b)       #Output:[1, 2, 3, 4, 5]
print(list_a)       #Output:[1, 3, 2, 5, 4]
list_a.sort()
print(list_a)       #Output:[1, 2, 3, 4, 5]

