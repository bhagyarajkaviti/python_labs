#You are given space-separated integers as input. Write a program to print the average of the given numbers.
numbers_list = input().split()

sum = 0
for i in numbers_list:
    i = int(i)
    sum += i
avg = sum/len(numbers_list)
print(round(avg,2))