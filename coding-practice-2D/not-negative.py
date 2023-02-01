#Write a program that reads two numbers A and B, and checks if both the given numbers are not negative.
a = int(input())
b = int(input())

result = (not(a < 0)) and (not(b < 0))

print(result)