#Given two integers M and N, write a program to print a solid rectangle pattern of M rows and N columns using the asterisk character (*).
#Note: Use For Loop

m = int(input())
n = int(input())

for i in range(m):
    print("* " * n)