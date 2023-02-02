#Write a program to print the smallest value among the three numbers A, B, and C.
A = int(input())
B = int(input())
C = int(input())

if A < B:
    smallest = A
else:
    smallest = B
if C < smallest:
    smallest = C
print(smallest)