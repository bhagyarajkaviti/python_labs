#Write a program that reads an M x N matrix and prints the perimeter of the matrix.
#Note
#The perimeter of the matrix is defined as the sum of all the elements on the four edges of the matrix.
#Input
#The first line of input contains space-separated integers
#representing M and N respectively.
#The next M lines of input contain N space-separated integers representing the matrix.

m, n = list(map(int,input().split()))
matrix = []
for i in range(m):
    rows = list(map(int, input().split()))
    matrix.append(rows)
#print(matrix)
perimeter = 0
for i in range(m):
    if i == 0 or i == m-1:
        perimeter += sum(matrix[i])
    else:
        perimeter += matrix[i][0] + matrix[i][n-1]
    
        
print(perimeter)