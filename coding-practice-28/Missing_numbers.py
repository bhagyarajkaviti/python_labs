#Write a program to find the missing numbers from 1 to the maximum number in the list.
num_list = input().split( )

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

last_item_in_num_list = num_list[len(num_list)-1]

new_full_num_list = []
for i in range(1, last_item_in_num_list +1):
    new_full_num_list.append(i)
new_full_num_set = set(new_full_num_list)

missing_num_list = sorted(new_full_num_set.difference(num_list))
print(missing_num_list)