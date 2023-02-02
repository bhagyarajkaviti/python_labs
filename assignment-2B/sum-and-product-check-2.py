#Write a program that reads two numbers A and B and checks if the sum of A and B is negative or the product of A and B is negative.
A = int(input())
B = int(input())

summation = A + B < 0
product = A * B < 0

result = summation or product
print(result)