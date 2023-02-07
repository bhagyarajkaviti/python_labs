#Write a program to print numbers from 1 to M in each column forming a rectangular pattern of M rows and N columns.
rows = int(input())
columns = int(input())

for i in range (1, rows+1):
    row_space = " "
    print((str(i)+ row_space) * columns)