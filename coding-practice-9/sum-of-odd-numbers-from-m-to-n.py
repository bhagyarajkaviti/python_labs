#Given two integers M and N, write a program to print the sum of the odd numbers from M to N.
m = int(input())
n = int(input())

sum = 0 
for i in range(m , n+1):
    if (i % 2 != 0):
       sum += i

print(sum)