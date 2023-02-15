#Write a program to find the Kth largest factor of the given number N.
#For example, if the given number N is 12 and K is 2, as the factors of 12 are 1, 2, 3, 4, 6, and 12, then the second-largest factor is 6. So the output should be 6.
n = int(input())
k = int(input())

factor = n
count = 0
kth_factor_found = False
for i in range(1, n +1):
    if not kth_factor_found: 
        if n % factor == 0:
            count = count + 1
        if count == k:
            print(factor)
            kth_factor_found = True
    factor = factor - 1

# another solution for the same question
    
#N = int(input())
#k = int(input())
#count = 0
#for i in range(N, 0, -1):
#    if((N % i) == 0):
#        count += 1
#    if(count == k):
#        print(i)
#        break

   