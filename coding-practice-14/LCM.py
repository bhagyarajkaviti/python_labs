#Write a program to find the Least Common Multiple of the given two numbers M and N.
#The least common multiple (L.C.M.) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.
m = int(input())
n = int(input())

if m > n:
    greatest = m
else:
    greatest = n

lcm_found = False # Initialize variable with the False boolean.
for number in range(greatest, (m * n + 1)):
    if not lcm_found: # Outer nested condition
        if (number % m == 0) and (number % n == 0): # Inner nested condition
            lcm_found = True # This boolean value stops the outer nested condition(if condition)
            lcm = number

if lcm_found:
    print(lcm)
else:
    print(m*n)
    
# another solution with some changes to the above solution
#m = int(input())
#n = int(input())

#if m > n:
#    greatest = m
#else:
#    greatest = n
#
#lcm_found = True
#for number in range(greatest, (m * n + 1)):
#    if lcm_found:
#        if (number % m == 0) and (number % n == 0):
#            lcm_found = False
#            lcm = number
#
#if lcm_found:
#    print(m * n)
#else:
#    print(lcm)