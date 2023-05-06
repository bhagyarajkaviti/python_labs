#Aman loves solving matrix problems. In one problem, he was given a M x N matrix and instructed to:
#• Identify the zeros and replace them with the sum of neighbouring elements (top, bottom, left and right elements).
#• Once all the zeroes are replaced, all the other elements in the corresponding row and column of those identified zeroes should be set to zero (excluding the elements which were previously zeros).
#Aman got stuck with this problem and your task is to help Aman solve this matrix problem.
#Write a program that reads the M x N matrix and prints the final matrix by following the above instructions.



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
        
        
        
        
        