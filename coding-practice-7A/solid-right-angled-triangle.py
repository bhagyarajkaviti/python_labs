#Given an integer number (N) as input. Write a program to print the right-angled triangular pattern of N lines using an asterisk (*) character.
N = int(input())

count = 1
while count <= N:
    print("* " * count)
    count = count + 1