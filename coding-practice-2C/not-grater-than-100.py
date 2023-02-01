#Write a program that reads two numbers A and B, and checks if the sum of A and B is not greater than 100.
number1 = int(input())
number2 = int(input())

result = (number1 + number2 > 100)
result = not(result)

print(result)