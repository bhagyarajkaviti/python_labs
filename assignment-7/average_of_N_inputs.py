#WGiven a number N, write a program that reads N inputs and prints the average of the N inputs.
n = int(input())

count = 0
sum = 0
while count < n:
    number = int(input())
    sum = sum + number
    count += 1
average = sum/n
print(average)