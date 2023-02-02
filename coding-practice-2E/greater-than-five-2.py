#write a program that reads three numbers A, B, and C, and checks if each of the given numbers is greater than 5.
A = int(input())
B = int(input())
C = int(input())

is_greater_than_5 = (A > 5) and (B > 5) and (C > 5)

print(is_greater_than_5)