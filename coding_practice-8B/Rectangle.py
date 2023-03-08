#Write a program that reads two numbers M and N, and prints a Rectangle of M rows and N columns using stars ( ).
rows = int(input())
columns = int(input())

for i in range(1, rows+1):
    print("*" * columns)