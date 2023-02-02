#Write a program that reads a four-digit number N and checks if N is an Armstrong Number.
#Note:
#   Armstrong Number:
    #A four-digit number N is an Armstrong Number if the number is equal to the sum of the 4th power of all digits.
    #Example:
    #1634 is an Armstrong Number as the sum of the 4th power of all digits of N is equal to 1634. (14+ 64+ 34+ 44 = 1634)
#Print Armstrong Number if N is an Armstrong number. Otherwise, print Not an Armstrong Number.
number = int(input())

number_string = str(number)

first_digit = int(number_string[0])
second_digit = int(number_string[1])
third_digit = int(number_string[2])
fourth_digit = int(number_string[3])

condition = (first_digit ** 4) + (second_digit ** 4) + (third_digit ** 4) + (fourth_digit ** 4) == number

if condition:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")