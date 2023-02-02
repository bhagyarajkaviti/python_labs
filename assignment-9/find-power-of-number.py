#Given an integer N, and exponent M as input, write a program to calculate N power M without using the power operator( ** ).
n = int(input())
m = int(input())

result = 1
for i in range(1,m+1):
    #result = result * n
    result *= n
print(result)