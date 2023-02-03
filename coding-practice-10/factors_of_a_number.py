#Write a program to print the factors of the given number. Note: A number F is considered as factor of the given number N, if N is exactly divisible by F (Remainder after dividing N with F is zero. N % F == 0)
n = int(input())

for factors in range(1, n+1):
    if n % factors == 0:
        print(factors)