#Write a program to print if the given number is a prime number.
#Note: A prime number is divisible only by itself and 1
n = int(input())

factors = 0
for i in range(2, n):
    if n % i == 0:
        factors = factors + 1

if factors == 0:
    print("Prime Number")
else:
    print("Not a Prime Numbers")