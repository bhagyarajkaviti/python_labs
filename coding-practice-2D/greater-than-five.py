#Write a program to check if both of the given numbers are positive and if atleast one of them is greater than 5.
#Note: Zero is not a positive number.
number1 = int(input())
number2 = int(input())

number_nature = (number1 > 0) and (number2 > 0)
condition_check = (number1 > 5) or (number2 > 5)

result = number_nature and condition_check
print(result)