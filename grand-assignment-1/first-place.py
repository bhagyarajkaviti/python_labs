#Write a program to print the given input word N times in a single line separated by space.
integer = int(input())
integer_string = str(integer)

if integer > 0:
    print(integer_string[len(integer_string) - 1])