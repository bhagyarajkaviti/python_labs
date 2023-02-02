#Write a program that reads the marks M in Maths, marks P in Physics and marks C in Chemistry and checks if any of the below conditions is satisfied.
#   M >= 60 and P >= 50 and C >= 45 and M+P+C >= 180.
#   M + P >= 120 or C+ P >= 110.
M = int(input())
P = int(input())
C = int(input())

condition1 = (M >= 60 and P >= 50 and C >= 45 and (M+P+C >= 180))
condition2 = (M + P >= 120) or (C+ P >= 110)

result = condition1 or condition2
print(result)