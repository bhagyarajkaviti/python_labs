#Write a program that reads a number N and prints two Right Angled Triangles of N rows, using numbers starting from 1.
n = int(input())

for i in range(1, n+1):
    print(str(i)* i)
for i in range(1, n+1):
    print(str(i)* i)