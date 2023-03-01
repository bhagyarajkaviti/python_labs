#Write a program that reads two numbers M and N and prints N numbers after M.
m = int(input())
n = int(input())

count = 1
while count <= n:
    print(m + count)
    count += 1