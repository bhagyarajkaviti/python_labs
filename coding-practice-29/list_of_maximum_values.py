#Write a program to create a list with maximum values in each list.
#Input:
#The first line of input will contain a positive integer N. The next N lines will contain space-separated integers.
#Output
#The output should be a single line containing the list of maximum values in each list.
n = int(input())

max_num_list = []
for i in range(n):
    num_list_str = input().split()
    for j in range(len(num_list_str)):
        num_list_str[j] = int(num_list_str[j])
    max_num = max(num_list_str)
    max_num_list.append(max_num)

print(max_num_list)