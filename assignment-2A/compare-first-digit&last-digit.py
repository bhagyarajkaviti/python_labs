#Write a program that reads two three-digit numbers A and B and checks if the first digit of A is less than the last digit of B.
number1 = int(input())
number2 = int(input())

number1 = str(number1)
number2 = str(number2)

result = (int(number1[0]) < int(number2[2]))
print(result)