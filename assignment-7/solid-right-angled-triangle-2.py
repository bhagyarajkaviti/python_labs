#Given an integer number N as input. Write a program to print the double triangular pattern of N lines using an asterisk( ) character as shown below.
#Note: There is a space after each asterisk character.
n = int(input())

count = 1
while count <= n:
    print("* " * count)
    count = count + 1
    
count = 1
while count <= n:
    print("* "* count)
    count = count + 1
        