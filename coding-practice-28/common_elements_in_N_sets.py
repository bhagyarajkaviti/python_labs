#Write a program to find the common elements in the N sets.
#Input:
#The first line of input will contain a positive integer (N).
#The next N lines will contain space-separated integers, denoting the elements of each set.
#Output
#The output should be a single line containing the list of common elements in N sets sorted in ascending order.
n = int(input())

all_input_lists = []
for i in range(n):
    input_list = input().split()
    for j in range(len(input_list)):
        input_list[j] = int(input_list[j])
    input_set = set(input_list)
    all_input_lists.append(input_set)
common_elements_set = all_input_lists[0]
for k in range(n-1):
    common_elements_set = common_elements_set.intersection(all_input_lists[k+1])
print(sorted(common_elements_set))
