#Write a program that reads two numbers A and B, and checks if one of the given numbers is a positive number.
number1 = int(input())
number2 = int(input())

result = (number1 > 0) or (number2 > 0)

print(result)