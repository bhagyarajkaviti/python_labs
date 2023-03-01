#Write a program that reads a number N and prints 10 numbers after N.
n = int(input())

count = 1
while count <= 10:
    print(n + count)
    count += 1