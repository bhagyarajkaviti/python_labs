#Write a program that reads two numbers A and B, and checks if both A and B are positive numbers or both A and B are less than 70.
A = int(input())
B = int(input())

result = ((A > 0) and (B >0)) or ((A < 70) and (B <70))

print(result)