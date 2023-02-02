#Write a program that reads a number N and checks if N is not divisible by all the given numbers 2, 3, 5 and 7.
number = int(input())

not_divisible_by_2 = number % 2 != 0
not_divisible_by_3 = number % 3 != 0
not_divisible_by_5 = number % 5 != 0
not_divisible_by_7 = number % 7 != 0

if not_divisible_by_7 and not_divisible_by_5 and not_divisible_by_3 and not_divisible_by_2:
    print("True")
else:
    print("False")