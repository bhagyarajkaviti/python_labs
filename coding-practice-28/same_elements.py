#Write a program to check if all the elements in a given list are same.
def str_to_int_convert(num_list):
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = input().split()
int_list = str_to_int_convert(num_list)
num_set = set(int_list)
if len(num_set) == 1:
    print(True)
else:
    print(sorted(num_set))