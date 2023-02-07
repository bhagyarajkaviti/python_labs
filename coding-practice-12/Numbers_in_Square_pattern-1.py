#Write a program to print numbers from 1 to N in each row forming a square pattern of N rows and N columns.
n = int(input())

result = ""
for  i in range(1, n+1):
    n_space = str(i) + " "
    result = result + n_space

for i in range(n):
    print(result)