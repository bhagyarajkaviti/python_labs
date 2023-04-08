#Given a M x N matrix, write a program to print the matrix after ordering all the elements of the matrix in increasing order.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain N space-separated integers, denoting the elements of each list.
#Output
#The output should be M lines containing the ordered matrix.
#Note: There is a space at the end of each line.
def str_to_int_list(num_list):
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

m,n = input().split()
m,n = int(m), int(n)

matrix = []
for i in range(m):
    num_list = input().split()
    int_list = str_to_int_list(num_list)

    matrix.extend(int_list)
sorted_matrix = sorted(matrix)
#print(sorted_matrix)

for i in range(m):
    row = []
    for j in range(n):
        j = n*i + j
        row.append(sorted_matrix[j])
    print(*row)

