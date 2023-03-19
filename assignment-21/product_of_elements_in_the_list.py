#You are given a space-separated list of integers as input. Write a program to print the product of these numbers.
numbers_list = input().split()

product = 1
for i in numbers_list:
    i = int(i)
    product *= i
print(product)