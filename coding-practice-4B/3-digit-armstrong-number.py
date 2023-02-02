#Write a program that reads a three-digit number N and checks if N is an Armstrong Number.
#NOTE:
    #Armstrong Number:
    #A three-digit number N is an Armstrong Number, if the sum of the cubes of all digits of N is equal to N
number = int(input())

number_string = str(number)
three_digit_check = len(number_string) == 3

first_digit = int(number_string[0])
second_digit = int(number_string[1])
third_digit = int(number_string[2])

condition = first_digit ** 3 + second_digit ** 3 + third_digit ** 3 == number

print(condition)