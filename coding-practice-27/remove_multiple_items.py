#For this problem, the prefilled code will contain a set. Write a program to remove a list of numbers if present in the set.
num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

input_list = input().split()
for i in range(len(input_list)):
    input_list[i] = int(input_list[i])

for item in input_list:
    num_set.discard(item)
num_list = list(num_set)
num_list.sort()
print(num_list)