#Write a program that reads a three-digit number N and checks if both the given conditions are satisfied.
    #Any of the digits of N is not equal to 5
    #N is between 300 and 700
#Print Valid Number if both the given conditions are satisfied. Otherwise, print Not a Valid Number.
A = int(input())

number = str(A)
length = len(number) == 3

first_digit = (int(number[0]) != 5)
second_digit = (int(number[1]) != 5)
third_digit = (int(number[2]) != 5)

condition1 = (first_digit or second_digit or third_digit)
condition2 = (A > 300 and A < 700)

if condition1 and condition2:
    print("Valid Number")
else:
    print("Not a Valid Number")