#Write a program to find the Kth largest factor of a number N.
n = int(input())
k = int(input())

factor = n
count = 0

for i in range(1, n +1):
    if n % factor == 0:
        count = count + 1
    if count == k:
        break
    factor = factor - 1
    
if count < k:
    print("1")
else:
    print(factor)