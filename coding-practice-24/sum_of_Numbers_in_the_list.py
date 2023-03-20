#Given space-separated numbers, write a program to print the sum of the given numbers.
numbers_list = input().split()

sum = 0
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
    sum += numbers_list[i]
print(sum)