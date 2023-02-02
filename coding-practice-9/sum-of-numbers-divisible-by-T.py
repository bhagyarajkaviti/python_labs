#Given three integers, write a program to print the sum of the numbers divisible by the given number T from M to N.
t = int(input())
m = int(input())
n = int(input())

sum = 0 
for i in range(m , n+1):
    if i % t == 0:
        sum += i
print(sum)