#Given an integer number N as input. Write a program to print the hollow right-angled triangular pattern of N lines as shown below.
#Note: There is a space after each asterisk ( ) character.
n = int(input())

for i in range(n):
    if i == 0: #1st line
        print("* " * n)
    elif i == n - 1: #last line
        print("  "* (n-1) + "* ")
    else: #hallow space part
        print("  " * i + "* " + "  " *(n - i - 2) + "* ")
               #left_space + (*) + hallow space + (*)     