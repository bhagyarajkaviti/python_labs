#Given integer N as input, write a program to display the sum of the first N terms in harmonic series.
#The series is: 1 + 1/2 + 1/3 + 1/4 + 1/5 ... + 1/N (N terms).

n = int(input())
sum_of_the_series = 0
for i in range(1, n+1):
    sum_of_the_series = sum_of_the_series + 1/i
output = round(sum_of_the_series, 2)    #print the sum of the series upto 2 decimal places
print(output)