#Given an integer number N as input. Write a program to print the hollow right-angled triangular pattern of N lines as shown below.
#Note: There is a space after each asterisk (*) character.
n = int(input())

for i in range(n):
    if i == 0:
        print("  " * (n - 1) + "* ")
    elif i == n - 1:
        print("* "* n)
    else:
        left_space = "  " * (n-1-i)
        hallo_space = "  " * (i - 1)
        print(left_space + "* " + hallo_space + "* ")