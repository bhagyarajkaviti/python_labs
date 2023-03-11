#Given a list of numbers, write a program to print the sum of the numbers in the list.
numbers_list = input().split(" ")

sum = 0
for i in numbers_list:
    i = int(i)
    sum += i
print(sum)