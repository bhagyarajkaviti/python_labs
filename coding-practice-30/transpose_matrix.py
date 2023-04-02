#For this problem, the prefilled code will contain an MXN matrix. Write a program to print the transpose of the matrix.
#Transpose of a matrix is obtained by changing rows to columns and columns to rows.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain N space-separated integers, denoting the elements of each list.
#Output
#The output should be N lines containing the transpose of the given matrix.
#Note: N is the length of a list in the matrix.

def get_transpose_of_matrix(matrix, m, n):
    # Complete this function
    for i in range(n):
        rows = []
        for j in range(m):
            rows.append(matrix[j][i])
        print(rows)

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

# Call the get_transpose_of_matrix function
get_transpose_of_matrix(num_list, m, n)