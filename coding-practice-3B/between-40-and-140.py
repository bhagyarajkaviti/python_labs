#Write a program that reads two numbers A and B and checks if any of the given numbers is between 40 and 140.
    #Print Between 40 and 140: Yes if any of the given numbers is between 40 and 140. Otherwise, print Between 40 and 140: No.
A = int(input())
B = int(input())

condition1 = A > 40 and A < 140
condition2 = B > 40 and B < 140

if condition1 or condition2:
    print("Between 40 and 140: Yes")
else:
    print("Between 40 and 140: No")