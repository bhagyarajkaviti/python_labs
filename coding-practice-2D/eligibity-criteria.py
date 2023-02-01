#Write a program that reads the marks in maths M,physics P, and chemistry C, and checks if any of the below conditions is satsfied.
#   M >= 70 and P >= 60 and C >= 60
#   M + P + C >= 180
M = int(input())
P = int(input())
C = int(input())

check_individual_subject = (M >= 70 and P >= 60 and C >= 60)
check_overall_marks = (M + P + C >= 180)

result = check_individual_subject or check_overall_marks
print(result)