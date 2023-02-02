#Write a program that reads the marks M in Maths and marks P in Physics and checks if both M and P are greater than 35 or sum of M and P is greater than or equal to 100.
#Print Qualified if both M and P are greater than 35 or sum of M and P is greater than or equal to 100. Otherwise, print Not Qualified.
M = int(input())
P = int(input())

condition = ((M > 35 and P > 35) or (M + P) >= 100)
if condition:
    print("Qualified")
else:
    print("Not Qualified")