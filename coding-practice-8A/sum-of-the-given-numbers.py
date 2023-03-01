#Given an integer N, write a program which reads N inputs and prints the sum of the given input integers.
#Note: Use For Loop
n = int(input())

sum = 0
for i in  range(n):
    number = int(input())
    sum = sum + number

print(sum)