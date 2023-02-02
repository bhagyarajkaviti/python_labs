#Write a program that reads three numbers A, B, and C, and checks if the difference between any two numbers (A-B, B-C and C-A) is always less than 25.
    #Print Difference is less than 25 if the difference between any two numbers (A-B, B-C and C-A) is always less than 25.Otherwise, print Difference is not less than 25.
A = int(input())
B = int(input())
C = int(input())

if ((A - B < 25) and (B - C < 25) and (C - A < 25)):
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")