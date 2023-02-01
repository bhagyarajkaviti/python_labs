#Write a program that reads two numbers A and B, and checks if any of the given numbers is not less than 15.
a = int(input())
b = int(input())

result = (not(a < 15)) or (not(b < 15))

print(result)