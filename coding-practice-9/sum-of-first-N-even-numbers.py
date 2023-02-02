#Given an integer (N) as input, write a program to print the sum of even numbers in the first N natural numbers.
n = int(input())

sum = 0
for i in range(n+1):
    if i % 2 == 0:
        sum += i

print(sum)