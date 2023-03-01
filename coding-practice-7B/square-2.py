#Write a program that reads a number N and prints a Square of N rows and N columns using numbers starting from 1.
#111
#222
#333
n = int(input())

count = 1
while count <= n:
    print(str(count) * n )
    count += 1