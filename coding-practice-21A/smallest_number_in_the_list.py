#Given space-separated numbers, write a program to print the Smallest number among the given numbers.
numbers_list = input().split()

Smallest = int(numbers_list[0])
for i in numbers_list[1:]:
    i = int(i)
    if i < Smallest:
        Smallest = i

print(Smallest)