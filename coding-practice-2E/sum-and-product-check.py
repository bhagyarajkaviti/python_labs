#Write a program that reads two numbers A and B and checks if both the sum and the product of the given numbers have less than three digits.
A = int(input())
B = int(input())

summation = A + B
summation = str(summation)

product = A * B
product = str(product)

result = (len(summation) < 3) and (len(product) < 3)
print(result)