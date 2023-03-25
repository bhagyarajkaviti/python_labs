#Given two lines of comma-separated integers, write a program to print the numbers that are present in both of the lines.
list_1 = input().split(",")
list_2 = input().split(",")

for i in range(len(list_1)):
    list_1[i] = int(list_1[i])
for i in range(len(list_2)):
    list_2[i] = int(list_2[i])

set_1 = set(list_1)
set_2 = set(list_2)

common_set = set_1 & set_2
common_list = list(sorted(common_set))

print(common_list)