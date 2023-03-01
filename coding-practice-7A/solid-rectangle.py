#Given two integers M and N, write a program to print a solid rectangle pattern of M rows and N columns using the asterisk character (*).
m = int(input())
n = int(input())

count = 1

while count <= m:
    print("* " * n)
    count = count + 1