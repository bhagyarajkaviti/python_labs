#Write a program to print numbers from 1 to N in each column forming a square pattern of N rows and N columns.
n = int(input())

for i in range(1, n+1):
    n_space = str(i) + " "
    result = n_space * n
    print(result)