#Set Operations : 1.Union           2.Difference
                # 3.Intersection    4.Symmetric Difference

#UNION:Union of two sets is a set containing all elements of both sets excluding duplicate elements.
    #Syntax: `set_a | set_b` or `set_a.union(sequence)`
#Example 1:
set_a = {4, 2, 8}
set_b = {1, 2}
union = set_a | set_b
print(union)        #Output:{1, 2, 4, 8}

#Example 2:
set_a = {4, 2, 8}
list_a = [1, 2]
union = set_a.union(list_a)
print(union)        #Output:{8, 1, 2, 4}

#INTERSECTION:Intersection of two sets is a set containing common elements of both sets excluding duplicate elements.
    #Syntax: `set_a & set_b` or `set_a.intersection(sequence)`
#Example 1:
set_a = {4, 2, 8}
set_b = {1, 2}
intersection = set_a & set_b
print(intersection)     #Output:{2}

#Example 2:
set_a = {4, 2, 8}
list_a = [1, 2]
intersection = set_a.intersection(list_a)
print(intersection)     #Output:{2}

#DIFFERENCE:Difference of two sets is a set containing 'all the elements in first set but not second list'.
    #Syntax: `set_a - set_b` or `set_a.difference(sequence)`
#Example 1:
set_a = {4, 2, 8}
set_b = {1, 2}
diff = set_a - set_b
print(diff)         #Output:{8, 4}

#Example 2:
set_a = {4, 2, 8}
tuple_a = (1, 2)
diff = set_a.difference(tuple_a)
print(diff)         #Output:{8, 4}

#SYMMETRIC DIFFERENCE:Symmetric difference of two sets is a set containing all elements which are 'not common to both sets'.
    #Syntax: `set_a ^ set_b` or `set_a.symmetric_difference(sequence)`
#Example 1:
set_a = {4, 2, 8}
set_b = {1, 2}
symmetric_diff = set_a ^ set_b
print(symmetric_diff)       #Output:{8, 1, 4}

#Example 2:
et_a = {4, 2, 8}
tuple_a = (1, 2)
diff = set_a.symmetric_difference(tuple_a)
print(diff)                 #Output:{8, 1, 4}
