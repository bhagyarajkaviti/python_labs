#Sets are basically `unordered` collection of items.
    # Every set element is 
        #Unique(no duplicates)
        #Must be immutable
#Set is created by enclosing elements within {curly} brackets. Each item is seperated by a comma.

#Example 1: creating a set
a = 2
set_a = {5, "six", a, 8.2}
print(type(set_a))      #Output:<class 'set'>
print(set_a)            #Output:{8.2, 2, 5, 'six'}  ===>Need not be in the same order as defined.

#Example 2: No Duplicate items. set elements should be Unique
set_a = {"a", "b", "a", "d", "c", "a", "b"}
print(set_a)            #Output:{'b', 'c', 'a', 'd'}
print(type(set_a))      #Output:<class 'set'>

#Example 3: Creating Empty set we use `set()` to create an empty set
set_a = set()
print(type(set_a))      #Output:<class 'set'> 
print(set_a)            #Output:set()
      
