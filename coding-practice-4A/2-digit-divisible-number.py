#Write a program that reads a two-digit number N and checks if N is divisible by both the digits of N.
#Print the double of N if N is divisible by both the digits of N. Otherwise, print N.
number = int(input())

number_string = str(number)
is_two_digit = len(number_string) == 2

first_digit = int(number_string[0])
second_digit = int(number_string[1])

if (number % first_digit == 0) and (number % second_digit == 0):
    print(number * 2)
else:
    print(number)