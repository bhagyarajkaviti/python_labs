#sequence_Membership_check
# Check of given data element is part of a sequence or not.
#Membership Operators: `in` and `not in`

#Example 1:
tuple_a = (1, 2, 3, 4)
is_part = 5 in tuple_a
print(is_part)      #Output:False
is_part = 1 not in tuple_a
print(is_part)      #Output:False

#Example 2:
list_a = [1, 2, 3, 4]
is_part = 1 in list_a
print(is_part)      #Output:True

#Example 3:
word = 'Python'
is_part = 'th' in word
print(is_part)      #Output:True