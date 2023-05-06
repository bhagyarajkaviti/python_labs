#Write a program that reads an N x N matrix and checks if it is a unique matrix or not.
#Note
#A Unique Matrix is a matrix in which every row and column contains all integers from 1 to N.
#Input
#The first line of input contains an integer representing N.
#The next N lines of input contain N space-separated integers representing the matrix.
#Output
#The output should be a single line containing a string, True should be print if the matrix is unique, otherwise False should be printed.

n = int(input())
numbers = set(range(1,n+1))
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
count = 0
for i in range(n):
    if numbers.issubset(matrix[i]):
        count += 1
if count == n:
    print(True)
else:
    print(False)