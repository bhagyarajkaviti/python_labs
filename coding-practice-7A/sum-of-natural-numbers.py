#Given an integer number (N) as input. Write a program to print the sum of first N natural numbers.
n = int(input())

count = 1
sum = 0
while count <= n:
    sum = sum + count
    count = count + 1
print(sum)