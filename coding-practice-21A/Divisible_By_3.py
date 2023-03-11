#Given space-separated numbers, write a program to print a list containing the given numbers that are divisible by 3
numbers_list = input().split()

devisible_by_3_list = []
for i in numbers_list:
    i = int(i)
    if i % 3 == 0:
        devisible_by_3_list += [i]
print(devisible_by_3_list)