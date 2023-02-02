#Write a  program that reads a three-digit number and checks if all the below conditions are satisfied.
#   The number contains 1.
#   The sum of all the digits of the number is less than 12.
#   The last digit of the number is equal to 5.
A = int(input())
A = str(A)
length = len(A) == 3

first_digit = int(A[0])
second_digit = int(A[1])
third_digit = int(A[2])

result = ((first_digit == 1) or (second_digit == 1) or (third_digit == 1)) and ((first_digit + second_digit + third_digit) <12) and (third_digit == 5)
print(result)