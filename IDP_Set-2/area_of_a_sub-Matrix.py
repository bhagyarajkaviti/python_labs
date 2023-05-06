#You are given an M x N matrix and a number K. In the given M x N matrix, you need to delete K rows from both the top and the bottom and delete K columns from both the left and the right. Finally, calculate the product of all elements in the resulting matrix.
#Write a program that reads an M x N matrix and a number K and prints the product of all elements in the resulting matrix.
#Input
#The first line of input contains two space-separated integers representing M and N respectively.
#The next M lines of input contain N space separated integers representing the matrix.
#The last line of input contains an integer representing K.

def find_area(matrix_table,z):
    if z > len(matrix_table)//2 or z > len(matrix_table[0])//2:
        return "0"
    elif z == 1 and len(matrix_table) == 2:
        return "0"
    else:
        result = 1 
        for i in range(z,len(matrix_table) - z):
            for j in range(z,len(matrix_table[i])- z):
                result *= matrix_table[i][j]
        return result 
values = list(map(int,input().split()))
x,y = values 
matrix_table = []
for i in range(x):
    each = list(map(int,input().split()))
    matrix_table.append(each)
z = int(input())
print(find_area(matrix_table,z))
        
        
        
        
        