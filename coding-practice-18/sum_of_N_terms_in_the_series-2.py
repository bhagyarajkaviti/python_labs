#Given two numbers X and N, write a program to find the sum of N terms in the given series. Then, print the sum by rounding up to 4 decimals in the given series.
x = float(input())
n = int(input())

sum = 0
for i in range(1,n+1):
    sum += x ** i
print(round(sum,4))