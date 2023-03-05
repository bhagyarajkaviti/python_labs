#Given two numbers N and S, write a program to find the sum of the given N numbers and round it up to 3 decimals. Check whether the sum that is rounded up to 3 decimals is equal to S or not.
#Print True if the sum of N inputs rounded up to 3 decimals is equal to S. Otherwise, print False.
n = int(input())
s = float(input())

sum = 0
for i in range(n):
    numbers = float(input())
    sum += numbers
if round(sum,3) == s:
    print(True)
else:
    print(False)