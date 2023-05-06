#Akshay has been given a few numbers. In the given numbers, every number except one will appear twice.
#Your task is to identify the number that appears exactly once.
#Write a program that reads the space-separated numbers and prints the number that appears exactly once.
#Input
#The input will be a single line containing space-separated integers representing numbers.
#Output
#The output should be a single line containing an integer, which is a number that appears only once.

num_list = list(map(int, input().split()))

only_once = []
for i in num_list:
    if num_list.count(i) == 1:
        only_once.append(i)
print(*only_once)