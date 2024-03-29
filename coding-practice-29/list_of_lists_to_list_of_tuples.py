#Write a program to convert the list of lists to a list of tuples.
#Input:
#The first line of input will contain an integer (N), denoting the number of lists.
#The next N lines will contain space-separated integers.
#Output:
#The output should be a single line containing a list with N tuples in the order of inputs given.

def convert_nested_list_to_list_of_tuples(nested_list):
    for i in range(len(nested_list)):
        nested_list[i] = tuple(nested_list[i])
    return nested_list


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


n = int(input())
num_list = []

for i in range(n):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)


tuples_list = convert_nested_list_to_list_of_tuples(num_list)
print(tuples_list)
