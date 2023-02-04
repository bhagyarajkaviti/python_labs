#Given an integer number N as input. Write a program to print the right-angled triangular pattern of N rows as shown below.
n = int(input())

for i in range(n+1):
    if i == 0:
        print("_"*(n + 1))
    else:
        hallow_space = " "*(n-i) 
        print("|" + hallow_space + "/")