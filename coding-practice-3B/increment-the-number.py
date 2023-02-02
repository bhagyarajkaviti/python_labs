#Write a program that reads a number N and checks if N is greater than 10.
    #Print the result of N+5 if N is greater than 10. Otherwise, print the result of N + 1.
number = int(input())

if number > 10:
    number = number + 5
    print(number)
else:
    number = number + 1
    print(number)