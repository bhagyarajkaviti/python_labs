#Given two integers M and N, write a program to print a hollow rectangle pattern of M rows and N columns using the asterisk character (*).
m = int(input())
n = int(input())

space = "  "
for i in range(1, m+1):
    if i == 1 or i == m:
        print("* " * n)
    else:
        print("* " + space * (n-2) + "* ")