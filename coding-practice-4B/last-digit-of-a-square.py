#Write a program that reads a number N and checks if the last digit of N is equal to the last digit of the square of N.
#Print Equal if the last digit of N is equal to the last digit of the square of N. Otherwise, print Not Equal.
number = int(input())

number_string = str(number)
last_digit_of_number = number_string[len(number_string) - 1:]

square_of_number = number ** 2
square_of_number_string = str(square_of_number)
last_digit_of_square = square_of_number_string[len(square_of_number_string) - 1:]

condition = last_digit_of_number == last_digit_of_square

if condition:
    print("Equal")
else:
    print("Not Equal")