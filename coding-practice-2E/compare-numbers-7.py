#Write a program that reads a four-digit number and checks if the first two digits of the number is 19 and the last two digits of the number is between 30 and 60.
A = int(input())
A = str(A)
length = len(A) == 4

first_two_digits = int(A[0:2]) == 19
last_two_digits = (int(A[2:]) > 30) and (int(A[2:]) < 60)

result = (first_two_digits and last_two_digits)
print(result)