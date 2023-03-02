#For this problem, the prefilled code will contain a list. Your program should create a new list with all the elements in existing list that are greater than given number.
#Note: The order of elements in the new list should be same as the order of those elements in the list given in the prefilled code.

num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
number = int(input())

output = []
for item in num_list:
    if item > number:
        output += [item]
print(output)