#Sets are Mutable
#In the set, the items are immutable but as a set it is mutable.
    # We can add and remove items from the set

#Example 1: adding items
    #Syntax: set_a.add(value)
    #adds the item to the set, if the item is not present already in the set
set_a = {1, 3, 6, 2, 9}
set_a.add(7)
print(set_a)        #Output:{1, 2, 3, 6, 7, 9}

#Example 2: adding multiple items
    #Syntax: set_a.update(sequence)
    #adds multiple items to the set, and duplicates are avoided.
set_a = set((1, 3, 6, 2, 9))
set_a.update([3, 4, 2, 7, 5, "p", "q"])
print(set_a)        #Output:{1, 2, 3, 4, 5, 6, 7, 'q', 9, 'p'}

#Example 3: Removing specific item 
    #syntax: set_a.discard(value)
    # Takes a single value and removes if present
set_a = {1, 3, 9}
set_a.discard(3)
print(set_a)        #Output:{1, 9}