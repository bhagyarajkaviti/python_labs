#Write a program that reads the marks in maths M, physics P, and chemistry C, and checks if all the below conditions are satisfied.
#   M + P >= 100 or P + C >=100 or M + C >= 100
#   M + P + C >= 180
M = int(input())
P = int(input())
C = int(input())

condition1 = (M + P >= 100) or (P + C >=100) or (M + C >= 100)
condition2 = (M + P + C >= 180)

result = condition1 and condition2
print(result)
