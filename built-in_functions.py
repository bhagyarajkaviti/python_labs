# min()

#Example 1:
smallest = min(3, 5, 6, 6, 9, 1,-84)
print(smallest)     #Output:-84

#Example 2:
smallest = min([3, 12, 6, 2, -9, 1,-4])
print(smallest)     #Output:-9

#Example 3:
smallest = min("java" , "python")
print(smallest)     #Output:java

# max()

#Example 1:
largest = max(3, 5, 6, 6, 9, 1,-84)
print(largest)     #Output:-9

#Example 2:
largest = max([3, 12, 6, 2, -9, 1,-4])
print(largest)     #Output:-12

#Example 3:
largest = max("java" , "python")
print(largest)     #Output:pyhton

# sum()

#Example 1:
sum_of_numbers = sum([1,4,-7,45,-9])
print(sum_of_numbers)   #Output:34

# sorted(sequuence)

#Example 1:
list_a = [3,4,5,7,8,8,9,2,3]
sorted_list = sorted(list_a)  #By default it is taken as `sorted(list_a, reverse=False)`
print(sorted_list)  #Output:[2, 3, 3, 4, 5, 7, 8, 8, 9]

#Example 2:
list_a = [3,4,5,7,8,8,9,2,3]
sorted_list = sorted(list_a, reverse=True)
print(sorted_list)  #Output:[9, 8, 8, 7, 5, 4, 3, 3, 2]