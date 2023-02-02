#Write a program that reads a number N and checks if N is divisible by 5 and 10.
#Print Divisible by 10 if N is divisible by 10.
#Print Divisible by 5 if N is divisible by 5 but not divisible by 10.
#Print Not Divisible by 10 or 5 if N is not divisible by 10 and N is not divisible by 5.
number = int(input())

if number % 10 == 0:
    print("Divisible by 10")
elif number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")