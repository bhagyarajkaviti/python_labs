#You are given space-separated integers as input. Write a program to print the maximum number among the given numbers.
numbers_list = input().split()

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
    
max_num = max(numbers_list)
print(max_num)