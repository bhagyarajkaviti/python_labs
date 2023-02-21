#Write a program to check if the given number is a prime number or not.
n = int(input())
is_prime = True
for i in range(2, n):
    if (n % i) == 0:
        is_prime = False
        break
print(is_prime)
