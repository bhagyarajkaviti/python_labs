#Write a program that reads a three-digit number and checks if each digit is greater than 4 or the first digit is equal to 6.
A = input()
three_digit_condition = (len(A) == 3)

first_digit = int(A[0]) > 4
second_digit = int(A[1]) > 4
third_digit = int(A[2]) > 4
is_first_digit_6 = int(A[0]) == 6

result = (first_digit and second_digit and third_digit) or (is_first_digit_6)
print(result)