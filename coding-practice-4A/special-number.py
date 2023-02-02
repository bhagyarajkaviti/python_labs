#Write a program that reads a two-digit number N and checks if any of the given conditions is satisfied.
    #The sum of digits of N is equal to 7.
    # One of the digits of N is equal to 7.
    #N is divisible by 7.
#Print Special Number if any of the given conditions is satisfied. Otherwise, print Normal Number.
number = int(input())

number_string = str(number)
is_two_digit = len(number_string) == 2

first_digit = int(number_string[0])
second_digit = int(number_string[1])

condition1 = first_digit + second_digit == 7
condition2 = first_digit == 7 or second_digit == 7
condition3 = number % 7 == 0

if condition1 or condition2 or condition3:
    print("Special Number")
else:
    print("Normal Number")