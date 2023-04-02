#For this problem, the prefilled code will contain two MXN matrices.
#Write a program to add the given two matrices.
#To add two matrices, just add the corresponding entries, and place this sum in the corresponding position in the result matrix.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain space-separated integers, denoting the elements of each list for first matrix.
#The next M following lines will contain space-separated integers, denoting the elements of each list for second matrix.
#Output
#The output should be M lines.
#Each line should contain a row in the matrix as a list after adding two matrices.

def add_two_matrices(first_matrix, second_matrix, m, n):
    # Complete this function
    for i in range(m):
        output_row = []
        for j in range(n):
            addition = first_matrix[i][j] + second_matrix[i][j]
            output_row.append(addition)
        print(output_row)

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


def read_matrix_inputs(m):
    num_list = []
    for i in range(m):
        list_a = input().split()
        list_a = convert_string_to_int(list_a)
        num_list.append(list_a)
    return num_list


m, n = input().split()
m, n = int(m), int(n)

first_matrix = read_matrix_inputs(m)
second_matrix = read_matrix_inputs(m)

# call the add_two_matrices matrices
add_two_matrices(first_matrix, second_matrix, m, n)