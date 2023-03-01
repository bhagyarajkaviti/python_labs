#Write a program that reads a number N and prints the average of N numbers from 1.
#Note
#The average of N numbers from 1 can be calculated as,
#Average = Sum of N numbers from 1 / Count of numbers (N)
#Example: If N = 3, the average of 3 numbers from 1 Average = (1 + 2 + 3) / 3 = 2.0
n = int(input())

count = 0
summ = 0
while count < n:
    count += 1
    summ += count
    average = summ/ count
print(average)