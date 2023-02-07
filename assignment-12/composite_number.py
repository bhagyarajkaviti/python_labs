#Given an integer N, write a program to find if the given number is a composite number or not. If it is composite, print True or else print False.
n = int(input())

factors = 0
for i in range(1, n+1):
    if n % i == 0:
        factors += 1
if factors > 2:
    print("True")
else:
    print("False")