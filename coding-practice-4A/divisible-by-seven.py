#Write a program that reads a number N and checks if the number N is divisible by 7.
#Print Divisible by Seven if N is divisible by 7. Otherwise, print Not Divisible by Seven.
number = int(input())

remainder = number % 7

if remainder == 0:
    print("Divisible by Seven")
else:
    print("Not Divisible by Seven")