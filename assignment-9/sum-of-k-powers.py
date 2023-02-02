#Write a program to print the sum of the Kth power of the first N natural numbers.
n = int(input())
power = int(input())

sum = 0
for i in range(1,n+1):
    sum += i ** power
    
print(sum)