#Given an integer number N as input. Write a program to print the right-angled triangular pattern of N lines as shown below.
#Note: There is a space after each asterisk (*) character.
n = int(input())

for i in range(n):
    if i == 0:
        print("* " * n)
    else:
        left_space = "  " * i
        print(left_space + "* " *(n - i))