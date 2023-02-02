#Write a program that reads two numbers A and B and checks if both the below conditions are satisfied.
#    One of A and B is less than 20.
#    One of A and B is greater than 30.
A = int(input())
B = int(input())

condition1 = (A < 20 or B < 20)
condition2 = (A > 30 or B > 30)

result = (condition1 and condition2)
print(result)