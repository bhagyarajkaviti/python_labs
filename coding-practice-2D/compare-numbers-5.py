#Write a program that reads two numbers A and B and checks if one of the given numbers is negative and product of the numbers is greater than or equal to -46.
number1 = int(input())
number2 = int(input())

number_check = (number1 < 0) or (number2 < 0)
product_check = (number1 * number2 >= -46)

result = number_check and product_check
print(result)