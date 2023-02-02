#Given two integers M and N, write a program to print the sum of the numbers from M to N.
m = int(input())
n = int(input())

sum = 0
for i in range(m, n+1):
    sum = sum + i
    
print(sum)