#For this problem, the prefilled code will contain an MXN matrix. Write a program to replace all elements of a given value with a new value.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain N space-separated integers, denoting the elements of each list.
#The next line of input will contain two space-separated integers, denoting the first value to be replaced by the second one.
#Output
#The output should be MXN matrix, with the value replaced at all places.

def replace_old_value_with_new_value(matrix, old_value, new_value):
    # Complete this function
    for each_list in matrix:
        for i in range(len(each_list)):
            if each_list[i] == old_value:
                each_list[i] = new_value
    return matrix
def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

values = input().split()
old_value, new_value = convert_string_to_int(values)

# Call the replace_old_value_with_new_value function
replaced_matrix = replace_old_value_with_new_value(num_list, old_value, new_value)
# Write your code here
for row in replaced_matrix:
    print(row)