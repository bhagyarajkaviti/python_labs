#Given an integer number (N) as input. Write a program to print the sum of first N natural numbers.
#Note: Use For Loop
n = int(input())

sum = 0
for i in range(1, n+1):
    sum = sum + i
    
print(sum)