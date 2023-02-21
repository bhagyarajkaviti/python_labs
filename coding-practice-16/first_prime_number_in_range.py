#Write a program to find the first prime number in the given range of M to N.
m = int(input())
n = int(input())

if not(m > 1):
    m = 2
    
no_primes = True # assuming there are no primes in a given range
for i in range(m, n+1):
    is_prime = True # assuming the number is prime
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
        no_primes = False   # This variable is used as a flag for if the given range is having prime numbers or not.
        break


if no_primes:
    print("No prime numbers in the given range")