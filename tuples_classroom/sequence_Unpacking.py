#sequence Unpacking: Values of any sequence can be directly assigned to variables.
#Note: The number of variables in the left should match the length of sequence.

#Example 1: unpacking tuples
tuple_a = ('R', 'e', 'd')       
s_1, s_2, s_3 = tuple_a         #the brackets are optional while creating tuples
print(s_1)      #Output:R
print(s_2)      #Output:e
print(s_3)      #Output:d

#Example 2: unpacking string
str_1 = "Blue"
(s_1, s_2, s_3, s_4) = str_1    
print(s_1)      #Output:B
print(s_2)      #Output:l
print(s_3)      #Output:u
print(s_4)      #Output:e

#Example 3: unpacking list
list_a = [1, 2, 3, 4]
s_1, s_2, s_3, s_4 = list_a
print(s_1)      #Output:1
print(s_2)      #Output:2
print(s_3)      #Output:3
print(s_4)      #Output:4

