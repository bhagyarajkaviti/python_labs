#Write a program that reads two numbers A and B, and checks if one of the below conditions is satisfied.
    # One of A and B is less than 20.
    # The sum of A and B is between 30 and 50.
#Print the sum of A and B if one of the given conditions is satisfied. Otherwise, print A and B on each line.
A = int(input())
B = int(input())

condition1 = A < 20 or B < 20
condition2 = A + B > 30 and A + B < 50

if condition1 or condition2:
    print(A + B)
else:
    print(A)
    print(B)