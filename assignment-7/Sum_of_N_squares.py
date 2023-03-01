#Write a program that reads a number N and prints the sum of squares of N numbers starting from 1.
n =int(input())

count = 1
sum = 0
while count <= n:
    sum += count ** 2
    count += 1
print(sum)