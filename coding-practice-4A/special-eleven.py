#Write a program that reads a number N and checks if the remainder is 0 or 1 when N is divided by 11.
#Print Special Eleven if the remainder is 0 or 1 when N is divided by 11. Otherwise, print Normal Number.
number = int(input())

condition = number % 11 == 0 or number % 11 == 1

if condition:
    print("Special Eleven")
else:
    print("Normal Number")