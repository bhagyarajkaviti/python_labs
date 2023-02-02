#Write a program that reads a two-digit number N and checks if any of the given conditions is satisfied.
    # The number N is divisible by 9.
    # One of the digits of the number N is equal to 9.
#Print Lucky Number if any of the given conditions is satisfied. Otherwise, print Unlucky Number.
number = int(input())

number_string = str(number)
is_two_digit = len(number_string) == 2

first_digit = int(number_string[0])
second_digit = int(number_string[1])

if (number % 9 == 0) or ((first_digit == 9 or second_digit == 9)):
    print("Lucky Number")
else:
    print("Unlucky Number")