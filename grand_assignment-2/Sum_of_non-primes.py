#Write a program to print the sum of non-primes in the given N numbers. The numbers which are not primes are considered as non- primes.
n = int(input())
sum = 0
for i in range(n):
    number = int(input())
    factors = 0
    for j in range(2, number):
         if number % j == 0:
             factors = factors + 1
    if factors == 0:
        pass
    else:
        sum = sum + number
print(sum)