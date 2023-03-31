#Write a program to print the lists which contain the unique elements in the given list of lists.
#Input
#The first line of input will contain a positive integer (N).
#The next N lines will contain space-separated integers, denoting elements of each list.
#Output
#The output should be a single line containing the list of lists with unique elements in the order of inputs given.

def str_to_int(num_list):
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

n = int(input())

unique_num_list = []
for i in range(n):
    num_list = input().split()
    int_list = str_to_int(num_list)
    if len(int_list) == len(set(int_list)):
        unique_num_list.append(int_list)

print(unique_num_list)
    