#Write a program to find the sum of odd numbers in first N natural numbers.
n = int(input())

sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        sum += i
print(sum)