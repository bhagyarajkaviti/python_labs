#Write a program that reads a three-digit number and checks if any of the below conditions is satisfied.
#   Each diit of the given number is greater than 7.
#   The product of any two digits is always less than or equal to 30.
A = int(input())
A = str(A)
length = len(A) == 3

first_digit = int(A[0])
second_digit = int(A[1])
third_digit = int(A[2])

condition1 = (first_digit > 7) and (second_digit > 7) and (third_digit > 7)
condition2 = (first_digit * second_digit <= 30) and (second_digit * third_digit <= 30) and (third_digit * first_digit <=30)

result = condition1 or condition2
print(result)