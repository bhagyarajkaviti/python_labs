#Write a program that reads a number N and prints the average of numbers from 1 to N.
n = int(input())

sum = 0
for i in range(1, n + 1):
    sum += i
average = sum/n
print(average)