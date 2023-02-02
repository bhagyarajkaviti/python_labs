#Write a program that reads two numbers A and B, and checks if A2+ B 2 (sum of the square of A and the square of B) is greater than or equal to 60.
#Print Greater than or Equal to 60 if the sum of the square of A and the square of B is greater than or equal to 60. Otherwise, print Less than 60.
A = int(input())
B = int(input())

condition = A ** 2 + B ** 2 >=60

if condition:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")