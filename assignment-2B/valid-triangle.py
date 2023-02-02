#Write a program that reads three sides A, B, and C of a triangle and checks if the sum of any two sides of the triangle is always greater than the third side.
A = int(input())
B = int(input())
C = int(input())

result = (A + B > C) and (B + C > A) and (C + A > B)
print(result)