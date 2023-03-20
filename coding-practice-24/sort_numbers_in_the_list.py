#Given comma-separated numbers, write a program to print a list containing the given numbers in Ascending order.
numbers_list = input().split(",")

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
Ascending_order = sorted(numbers_list)
print(Ascending_order)