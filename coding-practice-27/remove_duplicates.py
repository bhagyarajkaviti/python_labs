#Write a program to remove duplicate numbers in the list.
input_list = input().split()
for i in range(len(input_list)):
    input_list[i] = int(input_list[i])
remove_duplicate = set(input_list)
output_list = list(remove_duplicate)
output_list.sort()
print(output_list)