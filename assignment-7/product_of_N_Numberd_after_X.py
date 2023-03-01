#Write a program that reads two numbers X and N and prints the product of N numbers after X.
x = int(input())
n = int(input())

count = 1
product = 1
next_number = x
while count <= n:
    next_number = next_number + 1
    product = product * next_number
    count += 1
print(product)