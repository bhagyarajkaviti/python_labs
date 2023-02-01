#Write a program that reads three numbers A, B, and C, and checks if any of the given numbers is less than 15.
A = int(input())
B = int(input())
C = int(input())

result = (A < 15) or (B < 15) or (C < 15)

print(result)