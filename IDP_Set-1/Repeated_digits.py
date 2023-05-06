#Edward has been given a number that he must decode to obtain a PIN. He is required to find the count of repeated single-digit integers in the given number in order to decode it. Your task is to help Edward obtain a PIN.
#Write a program that reads the number and prints the count of repeated single-digit integers in the given number.
#Input
#The input will be a single line containing an integer representing the number.
#Output
#The output should be a single line containing an integer representing the count of repeated single-digit integers in the given number.

number_str = input()

num_list = []
for i in number_str:
    num_list.append(i)
num_set = set(num_list)
count = 0
for i in num_set:
    if num_list.count(i) > 1:
        count += 1
print(count)