#Write a program that reads a number and converts it to a positive number.
#   If the given number is negative , convert it to a positive number and print it. Otherwise, print the given number.
A = int(input())

if A < 0:
    # TODO: write code...
    A = A * (-1)
    print(A)
else:
    print(A)