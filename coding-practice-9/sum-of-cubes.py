#Write a program to print the sum of the cubes of the first N natural numbers.
n = int(input())

sum = 0
for i in range(1, n+1):
    cubes = i ** 3
    sum += cubes

print(sum)