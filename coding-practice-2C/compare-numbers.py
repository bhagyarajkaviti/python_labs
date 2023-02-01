#Write a program that reads two numbers A and B, and checks if both A and B are greater than 35 or A is greater than B.
number1 = int(input())
number2 = int(input())

result = (( number1 > 35) and (number2 > 35)) or (number1 > number2)

print(result)