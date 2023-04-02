#For this problem, the prefilled code will contain an MXN matrix. Write a program to print the maximum, minimum and sum of all elements in the matrix.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain N space-separated integers, denoting the elements of each list.
#Output
#The first line of output should be the maximum of all elements in the matrix.
#The second line of output should be the minimum of all elements in the matrix.
#The third line of output should be the sum of all elements in the matrix.

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
    num_list.extend(list_a)

# Write your code here
maxi = max(num_list)
print(maxi)
mini = min(num_list)
print(mini)
summation = sum(num_list)
print(summation)
