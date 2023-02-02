#write a program to ceck if the given two digit number is greater than 25 and its first digit is greater than its second digit.
A = int(input())

number = str(A)
first_digit = int(number[0])
second_digit = int(number[1])

result = (A > 25) and (first_digit > second_digit)
print(result)
