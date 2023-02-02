#Write a program that reads a number and checks if the given number is zero, positive or negative.
    #Print Zero if the given number is equal to 0.
    #Print Positive if the given number is greater than 0.
    #Print Negative if the given number is less than 0.
number = int(input())

if number == 0:
    print("Zero")
if number > 0:
    print("Positive")
if number < 0:
    print("Negative")