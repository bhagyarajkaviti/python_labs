#Given comma-separated numbers, write a program to print the Second Largest number in the given numbers.
numbers_list = input().split(",")

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

reverse_order = sorted(numbers_list, reverse=True)
print(reverse_order[1])