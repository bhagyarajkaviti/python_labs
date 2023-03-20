#Given comma-separated numbers and an index, write a program to print the Largest number among the numbers from the given index to the end of the list.
numbers_list = input().split(",")
n = int(input())

slice_list = numbers_list[n:]
maximum = max(slice_list)
print(maximum)