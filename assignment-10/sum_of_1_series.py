#Given integer N as input. Write a program to print the sum of series 1 + 11+ 111+.... N terms.
n = int(input())

sum = 0
for i in range(1, n+1):
    sum += int("1" * i)

print(sum)