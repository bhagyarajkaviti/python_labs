#Given comma-separated numbers, write a program to print a list containing given numbers in Descending order.
numbers_list = input().split(",")

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

Descending_order = sorted(numbers_list, reverse=True)
print(Descending_order)