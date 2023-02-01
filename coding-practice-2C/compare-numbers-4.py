#Write a program that reads two numbers A and B, and checks if one of A and B is less thhan 60 and one of A and B is greater than 80.
A = int(input())
B = int(input())

result = ((A < 60) or (B < 60)) and ((A > 80) or (B > 80))

print(result)