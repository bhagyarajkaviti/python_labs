#Given an integer number N as input. Write a program to print the double triangular pattern of N lines using an asterisk( ) character as shown below.
    #Note: There is a space after each asterisk * character.
    #Note: Use for-loop.
n = int(input())

for i in range(1, n+1):
    print("* " * i)
    
for j in range(1, n+1):
    print("* " * j)