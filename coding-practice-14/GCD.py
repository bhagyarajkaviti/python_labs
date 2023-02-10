#Write a program to find the Greatest Common Divisor of the given two numbers M and N.
#The greatest common divisor (G.C.D) of two numbers is the largest positive integer that perfectly divides the two given numbers.
m = int(input())
n = int(input())

if m > n:
    smallest = n
else:
    smallest = m
gcd = smallest

for i in range(1, smallest + 1):
    if (m % i) == 0 and (n % i) == 0:
        gcd = i
print(gcd)