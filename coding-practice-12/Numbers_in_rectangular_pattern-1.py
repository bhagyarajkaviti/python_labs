#Write a program to print numbers from 1 to N in each row forming a rectangular pattern of M rows and N columns.
m = int(input())
n = int(input())

result = ""
for j in range(1 , n+1):
    n_space = str(j) + " "
    result = result + n_space
    
for i in range(1, m+1):
    print(result)