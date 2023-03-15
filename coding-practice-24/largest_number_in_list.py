#Write a program to print the largest number in the list.
number_list = input().split(",")
int_number_list = []
for num in number_list:
    int_number_list += [int(num)]

maximum_number = max(int_number_list)
print(maximum_number)