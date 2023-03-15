#Write a program to print the difference between the largest and smallest numbers in the list.
numbers_list = input().split(",")

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
    
max_num = max(numbers_list)
min_num = min(numbers_list)

difference = max_num - min_num
print(difference)