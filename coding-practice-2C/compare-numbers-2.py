#Write a program that reads two numbers A and B, and checks if one of the given numbers is a negative number and the sum of the given numbers is greater than 7.
A = int(input())
B = int(input())

result = (( A < 0 ) or (B < 0)) and (A + B > 7)

print(result)