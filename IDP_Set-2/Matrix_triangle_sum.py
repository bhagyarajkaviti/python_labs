#Yash is solving a matrix problem as part of his entrance exam preparation.
#In that matrix problem, there is a square matrix of size N x N. Yash needs to calculate the sum of the upper and lower triangular elements of the matrix. Help Yash solve the given matrix problem.
#Write a program that reads the N x N matrix and prints the sum of the upper and lower triangular elements.
#Note
#The upper triangle consists of elements on the anti-diagonal and above on it.
#The lower triangle consists of elements on the anti-diagonal and below it.


n = int(input())

matrix = []
for i in range(n):
    rows = list(map(int, input().split()))
    matrix.append(rows)

#Upper Triangle sums
upper_triangle_sums = sum(matrix[0])  
for i in range(n):  
    upper_triangle_sums += sum(matrix[i][:-i])

#LOwer Triangle Sums
lower_triangle_sums = 0
for i in range(n):
    lower_triangle_sums += sum(matrix[i][-i-1:])

print(upper_triangle_sums)
print(lower_triangle_sums)