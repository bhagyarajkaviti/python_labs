#Given two integers M, N . Write a program to print the product of numbers in the range M and N (inclusive of M and N ).
m = int(input())
n = int(input())

result = 1
for i in range (m , n+1):
    result *= i

print(result)