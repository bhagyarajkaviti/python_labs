#Given space-separated numbers, write a program to print a list containing the given numbers.
numbers_list = input().split(" ")
len_of_number_list = len(numbers_list)

final_list = []
for i in range(len_of_number_list):
    integer = int(numbers_list[i])
    final_list += [integer]
print(final_list)
