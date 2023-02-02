#Write a program that reads a three-digit number and checks if all the digits of the number are the same.
number = int(input())
A = str(number)

three_digit = len(A) == 3

result = (int(A[0]) == int(A[1]) == int(A[2]))
print(result)
