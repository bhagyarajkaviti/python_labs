#Given a MXN matrix,write a program to print all Anti-Diagonals elements of matrix
#Input
#The first line of input will contain a M, N values separated by space. The second line will contain matrix A of dimensions MxN.
#Output
#The output should contain anti-diagonal elements separated by a line.
def convert_str_to_int_list(num_list):
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list
    
def print_anti_diagonals_elements(m,n,matrix):
    for k in range(m+n-1):
        anti_diagonal_elements = []
        for i in range(m):
            for j in range(n):
                if k == i + j:
                    anti_diagonal_elements.append(matrix[i][j])
    
        print(*anti_diagonal_elements)


m,n = input().split()
m, n = int(m), int(n)
matrix = []
for i in range(m):
    num_list = input().split(" ")
    int_list = convert_str_to_int_list(num_list)
    matrix.append(int_list)
    
print_anti_diagonals_elements(m,n,matrix)