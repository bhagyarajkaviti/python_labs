# A list which is an item of another list is called Nested list

#Example 1: Accessing items of nested list
list_a = [5, "six", [8,6], 8.2]
print(list_a[2])        #Output:[8, 6]
print(list_a[2][0])     #Output:8
list_b = [9, "seven", [8, 6, [18, 52]], 9.4]
print(list_b[2][2][1])  #Output:52

#Example 2: Accessing items of nested sequence
list_a = [5, (8, 6, 9, 67,"nine")]
print(list_a[1][4])     #Output:nine
list_b = ["five", "six"]
print(list_b[0][2])     #Output:v





