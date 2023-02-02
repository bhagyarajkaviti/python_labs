#Write a program that reads the marks M in Maths, marks P in Physics and marks C in Chemistry and checks if both the below conditions are satisfied.
#   M >= 35 and P >= 35 and C >= 35.
#   M + P >= 90 or P+C>= 90 or M + C >= 90.
M = int(input())
P = int(input())
C = int(input())

condition1 = (M >= 35 and P >= 35 and C >= 35)
condition2 = (M + P >= 90) or (P + C >= 90) or (M + C >= 90)

result = condition1 and condition2
print(result)