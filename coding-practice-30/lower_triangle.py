#For this problem, the prefilled code will contain an MXN matrix. Write a program to print the lower triangle of the matrix. Lower triangular matrix is a matrix which contain elements below principle diagonal including principle diagonal elements.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain N space-separated integers, denoting the elements of each list.
#Output
#The output should be M rows containing the elements in the form of a lower triangle.

def print_lower_triangle(matrix):
    # Complete this function
    for i in range(len(matrix)):
        row_list = matrix[i][:i+1]
        print(row_list)

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

# Call the print_lower_triangle function
print_lower_triangle(num_list)