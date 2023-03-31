#Write a program to read N lines of inputs and create a nested list with each line as a list.
n = int(input())

nested_num_list = []
for i in range(n):
    num_list_str = input().split()
    for j in range(len(num_list_str)):
        num_list_str[j] = int(num_list_str[j])
    nested_num_list.append(num_list_str)

print(nested_num_list)
    