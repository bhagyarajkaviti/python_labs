#Write a program to print the sum of the squares of the first N natural numbers.
n = int(input())

sum = 0
for i in range(1, n+1):
    squares = i ** 2
    sum += squares

print(sum)