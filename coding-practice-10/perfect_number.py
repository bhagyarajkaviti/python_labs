#Write a program to check whether the given number is a perfect number or not.
#A number is considered as a Perfect number if sum of all factors excluding itself is equal to the number.
n = int(input())

sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")