#Given an integer number (N) as input. Write a program to print the right-angled triangular pattern of N lines using an asterisk (*) character.
#Note: Use For Loop

n = int(input())

for i in range(n):
    i = i + 1
    print("* " * i)
    