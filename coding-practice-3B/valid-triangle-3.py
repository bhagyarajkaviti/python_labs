#Write a program that reads three sides A, B, and C of a triangle and checks if the sum of any two sides of the triangle is always greater than the third side.
    #Print It's a Triangle if the sum of any two sides of the triangle is always greater than the third side. Otherwise, print It's not a Triangle.
A = int(input())
B = int(input())
C = int(input())

if (A + B > C) and (B + C > A) and (C + A > B):
    print("It's a Triangle")
else:
    print("It's not a Triangle")