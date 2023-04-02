#For this problem, the prefilled code will contain an MXN matrix. Write a program to print the maximum, minimum and sum for each row in the matrix.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain N space-separated integers, denoting the elements of each list.
#Output
#The first line of output should contain the list of the maximum number in each row.
#The second line of output should contain the list of minimum number in each row.
#The third line of output should contain the list of the sum of each row.

def print_max_min_sum_for_row_wise(num_list):
    # Complete this function
    row_maximum = []
    row_minimum = []
    row_sum = []
    for each_list in num_list:
        row_maximum.append(max(each_list))
        row_minimum.append(min(each_list))
        row_sum.append(sum(each_list))
    
    print(row_maximum)
    print(row_minimum)
    print(row_sum)

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

print_max_min_sum_for_row_wise(num_list)
