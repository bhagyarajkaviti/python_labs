#Write a program that reads two numbers M and N and prints the sum of N numbers from M.
m = int(input())
n = int(input())

count = 0
sum = 0
while count < n:
    sum = sum + m + count
    count += 1
print(sum)