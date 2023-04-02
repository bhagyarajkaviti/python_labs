#For this problem, the prefilled code will contain an MXN matrix. Write a program to print the list of elements of principal diagonal in the matrix.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain N space-separated integers, denoting the elements of each list.
#Output
#The output should be a single line containing the list of principal diagonal elements.

def get_principal_diagonal_elements(matrix, m, n):
    # Write your code here
    principal_diagonal = []
    for i in range(m):
        if i<n:
            principal_diagonal.append(matrix[i][i])
    return principal_diagonal

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
#print(num_list)
# Call the get_principal_diagonal_elements function
print(get_principal_diagonal_elements(num_list, m, n))