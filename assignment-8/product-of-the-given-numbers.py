#Given an integer N, write a program that reads N inputs and prints the product of the given input integers.
#Note: Use for-loop.
n = int(input())
multiplication = 1
for i in range(n):
    m = int(input())
    multiplication = multiplication * m
print(multiplication)