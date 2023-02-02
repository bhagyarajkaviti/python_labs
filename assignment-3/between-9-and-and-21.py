#Write a program that reads three numbers A, B, and C and checks if any of the given numbers is between 9 and 21.
A = int(input())
B = int(input())
C = int(input())

condition = (A > 9 and A < 21) or (B > 9 and B < 21) or (C > 9 and C < 21)

if condition:
    print("True")
else:
    print("False")