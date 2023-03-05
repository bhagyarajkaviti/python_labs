#Given two numbers M and N, write a program to print the sum and average of the numbers from M to N each on a new line.
m = int(input())
n = int(input())

sum = 0
count = 0
for i in range(m, n+1):
    sum = sum + i
    count += 1
print(sum)
average = sum/count
print(average)