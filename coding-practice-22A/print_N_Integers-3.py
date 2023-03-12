#A function is given in the prefilled code that takes a number N as an argument.
#Write a program to print the numbers from 1 to the given number N, each on a new line.
def print_numbers(number):
    for i in range(1,number+1):
        print(i)
    # complete this function
number = int(input())
# call the print_numbers function
print_numbers(number)