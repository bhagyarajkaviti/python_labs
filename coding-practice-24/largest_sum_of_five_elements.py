#Given comma-separated numbers, write a program to print the maximum possible sum with 5 numbers of the given comma-separed numbers.
numbers_list = input().split(",")

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

reverse_order = sorted(numbers_list, reverse=True)
print(sum(reverse_order[:5]))