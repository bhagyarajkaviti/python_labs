#Set comparisions are used to validate whether one set fully exists within another.
    # `issubset()`          #`issuperset()`         #`isdisjoint()` these returns booleans

#SUBSET:
    #Syntax:`set_2.issubset(set_1)`
#Example 1:
set_1 = {'a', 1, 3, 5}
set_2 = {'a', 1}
is_subset = set_2.issubset(set_1)
print(is_subset)        #Output:True       

#Example 2:
set_1 = {4, 6}
set_2 = {2, 6}
is_subset = set_2.issubset(set_1)
print(is_subset)        #Output:False

#SUPERSET:
    #Syntax:`set_1.issuperset(set_2)`
#Example 1:
set_1 = {'a', 1, 3, 5}
set_2 = {'a', 1}
is_superset = set_1.issuperset(set_2)
print(is_superset)      #Output:True 

#Example 2:
set_1 = {4, 6}
set_2 = {2, 6}
is_superset = set_1.issuperset(set_2)
print(is_superset)        #Output:False

#DISJOINT SET: Returns `True` when two sets have no common elements. else,`False`
    #Syntax:`set1.isdisjoint(set2)` or `set2.isdisjoint(set1)`
#Example 1:
set_a = {1, 2}
set_b = {3, 4}
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)          #Output:True

#Example 2:
set_a = {4, 6}
set_b = {2, 6}
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)          #Output:False